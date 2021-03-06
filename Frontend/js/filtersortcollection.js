var selectedWine;

window.init = function() {
	"use strict";
	var resultswidth = $("#results").width();
	var relayout480 = false;
	var map;
	var wines;
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
		if($("#filterselector").height() < $("#filterselector").next().height() && $(window).width() > 765) {
			var navbaroffset = 0;
			if($(".navbar-fixed-top").css("position") === "fixed") {
				navbaroffset = $(".navbar-fixed-top").height();
			}
			if(!$("#toolbarspacer").hasClass("show") && $(window).scrollTop() > $("#toolbarspacer").offset().top) {
			    $("#toolbarspacer").addClass("show");
			    $("#results").isotope("reLayout");
			}
			if($("#toolbarspacer").hasClass("show") && $(window).scrollTop() <= $("#toolbarspacer").offset().top) {
			    $("#toolbarspacer").removeClass("show");
			}
			if($(window).scrollTop()+navbaroffset+25 > $("#filterselector").offset().top) {
				if($("#filterselector .well").offset().top + $("#filterselector .well").height() >= $("#filterselector").next().height() + $("#filterselector").next().offset().top) {
					$("#filterselector .well").addClass("filterfixedbottom");
				}
				if($("#filterselector .well").offset().top > $(window).scrollTop()+navbaroffset+25){
					$("#filterselector .well").removeClass("filterfixedbottom");
				}
				$("#filterselector .well").addClass("filterfixed");
				$("#toolbar").addClass("affix");
			} else {
				$("#filterselector .well").removeClass("filterfixed").removeClass("filterfixedbottom");
				$("#toolbar").removeClass("affix");
			}	
		} else {
			$("#filterselector .well").removeClass("filterfixed");
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
		event.preventDefault();
		if($(".selected").length === 0) {
			$("#noneselected").modal();
            return;
		}
        var selected = $(".selected").map(function(){
                        return $(this).data('id');
                       });
        $.cookie('toprint', JSON.stringify(selected.toArray()));
        window.location="print.html";
	});
	$("a[href='#print']").click(function(event) {
		event.preventDefault();
        $.cookie('toprint', '[]');
        window.location="print.html";
	});
	$(".pronounciation").tooltip();
	$("#togglefilters").click(function(event) {
		$("#filterselector").toggle();
		$("#togglefilters span.hide").toggle();
		$("#togglefilters span:not(.hide)").toggle();
	});
	$('#wine-name-input').typeahead({
        source: function (query, process) {
        	$("#add-wine-name-button").addClass("disabled").html("Loading");
        	backend.Wine.get({name__istartswith:query.trim(), limit: 5}, function(data) {
        		$("#add-wine-name-button").removeClass("disabled").html("&nbsp;&nbsp;&nbsp;Add&nbsp;&nbsp;&nbsp;");
	        	wines = [];
                map = {};
                $.each(data, function (i, wine) {
                    wines.push(wine.name);
                    map[wine.name] = wine;
                });
                console.log(wines);
                console.log(map);
                process(wines);
        	});
        },
        updater: function (item) {
            selectedWine = map[item];
            return item;
        }
    });
};

$(document).ready(window.init);

function updateResults() {
	"use strict";
	var filters = [];
	$("#filterselector a.checked").each(function() { 
		filters.push(hyphenate($(this).text().trim()));
	});
	if(filters.length === 0) {
		filters = "";
	} else {
		filters = "." + filters.join(",.");
	}
	$('#results').isotope({ filter: filters });
	console.log(filters);
}
