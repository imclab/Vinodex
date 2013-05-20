window.init = function() {
	"use strict";
	var resultswidth = $("#results").width();
	var relayout480 = false;
	$(".winery").each(function() {
		$(this).parent().addClass($(this).text().toLowerCase().trim().replace(/ /g, "-"));
	});
    $('#logout').click(function(event){
      event.preventDefault();
      backend.logout();
      window.location="/";
    });
	$("#filterselector").on("click", "a", function(event) {
		event.preventDefault();
		$(this).toggleClass("checked");
		updateResults();
	});
	$(".sortoptions").on("click", ".sortoption a", function(event) {
		event.preventDefault();
		if($(this).attr('data-sort-attr') !== undefined) {
			console.log($(this).data('sort-attr'));
			$('#results').isotope({ 
				sortBy : $(this).data('sort-attr') 
			});
		} else if($(this).data('sort-order') === "asc"){
			console.log($(this).parent().parent().siblings("a").data('sort-attr'));
			$('#results').isotope({ 
				sortBy : $(this).parent().parent().siblings("a").data('sort-attr'),
				sortAscending: true
			});
		} else {
			console.log($(this).parent().parent().siblings("a").data('sort-attr'));
			$('#results').isotope({ 
				sortBy : $(this).parent().parent().siblings("a").data('sort-attr'),
				sortAscending: false
			});
		}
	});
	$(window).resize(function(){
		if($(".gridbtn").hasClass("active") && resultswidth !== $('#results').width()) {
			$('#results').isotope({
				cellsByRow: { 
					columnWidth: $('#results').width() / cellsPerRow(),
					rowHeight: 270
				}
			});
			resultswidth = $('#results').width();
		}
		if(!relayout480 && $(".tablebtn").hasClass("active") && $('#results').width() <= 480) {
			relayout480 = true;
			$('#results').isotope("reLayout");
		} else {
			relayout480 = false;
		}
	});
	$(window).scroll(function() {
		if(!$("#toolbarspacer").hasClass("show") && $(window).scrollTop() > 275) {
			$("#toolbarspacer").addClass("show");
			$("#results").isotope("reLayout");
		}
		if($("#toolbarspacer").hasClass("show") && $(window).scrollTop() <= 275) {
			$("#toolbarspacer").removeClass("show");
		}
		if($("#loading").is(":not(:visible)") && $(window).scrollTop()+$(window).height() > $("#results").offset().top+$("#results").height()) {
			$("#loading").show();
		}
		if($("#loading").is(":visible") && $(window).scrollTop()+$(window).height() <= $("#results").offset().top+$("#results").height()) {
			$("#loading").hide();
		}
	});
	$(".gridbtn").click(function(event) {
		$("#results").addClass("gridview").removeClass("tableview").isotope({
			layoutMode: 'cellsByRow',
			cellsByRow: {
				columnWidth: $('#results').width() / cellsPerRow(),
				rowHeight: 270
			}
		});
		event.preventDefault();
	});
	$(".tablebtn").click(function(event) {
		$("#results").addClass("tableview").removeClass("gridview").isotope({
			layoutMode: 'straightDown',
			straightDown: {
				rowHeight: 100
			}
		});
		event.preventDefault();
	});
	$("#selectall").click(function(event) {
		event.preventDefault();
		$(".result").addClass("selected");
	});
	$("#selectnone").click(function(event) {
		event.preventDefault();
		$(".result").removeClass("selected");
	});
	$("a[href='#deletewine']").click(function(event) {
		if($(".selected").length === 0) {
			$("#noneselected").modal();
		} else if($(".selected").length === 1) {
			$("#deletewine").modal();
			$("#deletewine").addClass("singular").removeClass("plural");
		} else {
			$("#deletewine").modal();
			$("#deletewine").addClass("plural").removeClass("singular");
		}
		event.preventDefault();
	});
	$("a[href='#printselected']").click(function(event) {
		if($(".selected").length === 0) {
			$("#noneselected").modal();
		}
		event.preventDefault();
	});
	$("a[href='#uploadimage']").click(function(event) {
		event.preventDefault();
		$(this).next().click();
	});
	$("#validatelogin").click(function(event) {
        /**
         * TODO: Handle login failure
         */
        event.preventDefault();	
		$("#loginmodal").valreset();
		$("#login").valreset();
		var email = $("#loginemail").valemail();
		var pass = $("#loginpassword").valpassword();
        var emailVal = $("#loginemail").val();
        var passwordVal = $("#loginpassword").val();
        backend.login(emailVal, passwordVal, function(){
          window.location = "collection.html";
        }, function(){console.log("Login Failed");});
	});
	$("#validatesignup").click(function(event) {
        /**
         * TODO: Handle account creation failure
         */
        event.preventDefault();
		$("#signup").valreset();
		var name = $("#signupname").vallength();
		var email = $("#signupemail").valemail();
		var pass = $("#signuppassword").valpassword();
		if(name || email || pass) {
          return;
		}
        var nameVal = $("#signupname").val();
        var emailVal = $("#signupemail").val();
        var passwordVal = $("#signuppassword").val();
        backend.createUserAccount(nameVal, emailVal, passwordVal, function(){
          window.location = "collection.html";
        }, function(){console.log("Account Creation Failed");});
	});
	$("#forgotpassval").click(function(event) {
		$("#login").valreset();
		if($("#forgotemail").valemail()) {
			event.preventDefault();	
		}
	});
	$("#valaddwine").click(function(event) {
		$("#addwine").valreset();
		var name = $("#winename").vallength();
		var year = $("#year").valvintageyear();
		var alcohol = $("#alcoholcontent").vallength();
		var cellar = $("#cellar").valselect();
		var type = $("#winetype").valselect();
		var bottles = $("#numbottles").vallength();
		if(name || year || alcohol || cellar || type || bottles) {
			event.preventDefault();	
		}
	});
};
$(document).ready(window.init)

function updateResults() {
	"use strict";
	var filters = [];
	$("#filterselector a.checked").each(function() { 
		filters.push($(this).text().toLowerCase().trim().replace(/ /g, "-"));
	});
	if(filters.length === 0) {
		filters = "";
	} else {
		filters = "." + filters.join(",.");
	}
	$('#results').isotope({ filter: filters });
	console.log(filters);
}

jQuery.fn.valreset = function() {
    $(this).find(".control-group").removeClass("error");
	$(this).find(".help-block").addClass("hide");
};

jQuery.fn.vallength = function() {
    if($(this).val().trim().length === 0) {
	    $(this).valerror();
	    return true;
    } else {
	    return false;
    }
};

jQuery.fn.valvintageyear = function() {
    if($(this).val().trim().length === 0 && !$("#nv").prop("checked")) {
	    $(this).valerror();
	    return true;
    } else {
	    return false;
    }
};

jQuery.fn.valemail = function() {
    if($(this).val().indexOf("@") === -1) {
	    $(this).valerror();
	    return true;
    } else {
	   	return false;
    }
};

jQuery.fn.valpassword = function() {
    return $(this).vallength();
};

jQuery.fn.valselect = function() {
    if($(this).val() === null) {
	    $(this).valerror();
	    return true;
    } else {
	   	return false;
    }
};

jQuery.fn.valerror = function() {
	if($(this).parent().hasClass("input-append")) {
		$(this).parent().siblings(".help-block").removeClass("hide").parent().parent().addClass("error");
	} else {
		$(this).siblings(".help-block").removeClass("hide").parent().parent().addClass("error");
	}
};
