window.init = function() {
	"use strict";
	$('#logout').click(function(event){
		event.preventDefault();
		backend.logout();
		window.location="/";
	});
	$("#validatelogin").click(function(event) {
		/**
		* TODO: Handle login failure
		*/
		event.preventDefault();	
		$("#loginmodal").valreset(); // reset error conditions before checking again
		$("#login").valreset();
		var email = $("#loginemail").valemail();
		var pass = $("#loginpassword").valpassword();
        if (!email || !pass){
          return;
        }
		/**
		* validation functions return null on invalid input nowm
		* in addition to putting errors on the fields
		* return the actual values on valid input
		*/
		backend.login(email, pass, function(){
			window.location = "collection.html";
		}, function(response){

          if (response.status == C.UNAUTHORIZED) {
            $("#loginpassword").valerror("wrongpassword");
          }

          if (response.status == C.NOT_FOUND) {
            $("#loginemail").valerror("userdoesnotexist");
          }
        });
	});
	$("#validatesignup").click(function(event) {
		/**
		* TODO: Handle account creation failure
		*/
		if($(this).hasClass("disabled")) {
			return;
		}
		event.preventDefault();
		$("#signup").valreset();
		var name = $("#signupname").vallength();
		var email = $("#signupemail").valemail();
		var pass = $("#signuppassword").valpassword();
		if(name !== null && email !== null && pass !== null) {
			$(this).addClass("disabled").html("Signing Up...");
			$(this).next().toggle();
		} else {
          return;
        }
		backend.createUserAccount(name, email, pass, function(){
			window.location = "collection.html";
		}, function(){
            $("#signupemail").valerror("useralreadyexists");
			$("#validatesignup").removeClass("disabled").html("Sign Up");
			$("#validatesignup").next().toggle();
		});
	});
	$("#validatepasschange").click(function(event) {
		event.preventDefault();
		$("#passchange").valreset();
		var pass = $("#passchangepass").valpassword();
	});
	$("#addannotation .nav-tabs").click(function() {
		$("#addannotation").valreset();
	});
	$("#validateannotation").click(function(event) {
		event.preventDefault();
		$("#addannotation").valreset();
		var tab = $("#addannotation .nav-tabs .active a").attr("href");
		var tastenotes = $("#tastenotes").vallength();
		var winerating = $("#winerating").valrating();
		var removereason = $("#removeaction").html();
		var removequantity = $("#removequantity").valnumber();

        var closeModal = function(){
          console.log("Close modal");
          $("#addannotation").modal('hide');
          renderPage()
        } 

        var bottleId = parseInt(frontend.getHash());

        if (tab == "#notes" && tastenotes){
          backend.Annotation.create({
            bottle: {id: bottleId},
            key: "Taste Notes",
            value: tastenotes
          }, closeModal) 
        }

        if (tab == "#remove" && removereason && removequantity){
          backend.removeBottles(bottleId, removereason, removequantity, closeModal);
        }

        if (tab == "#rate" && winerating){
          backend.Bottle.update(bottleId, {rating: winerating}, closeModal)
        }

	});
	$("#removereason a").click(function () {
		console.log("clicked");
		$("#removeaction").html($(this).html());
	});
	$("#forgotpassval").click(function(event) {
		$("#login").valreset();
		var email = $("#forgotemail").valemail();
	});
	$('#tabs a').click(function (event) {
		event.preventDefault();
		$(this).tab('show');
	});
	var rated = false;
	$("#rate .icon-star-empty").hover(function() {
		if(!rated) {
			$(this).toggleClass("icon-star").toggleClass("icon-star-empty");
			$(this).prevAll().toggleClass("icon-star").toggleClass("icon-star-empty");
		}
	});
	$("#rate").on("click", ".icon-star, .icon-star-empty", function(event) {
		rated = true;
		$(this).siblings().removeClass("icon-star").addClass("icon-star-empty");
		$(this).addClass("icon-star").removeClass("icon-star-empty");
		$(this).prevAll().addClass("icon-star").removeClass("icon-star-empty");
	});
	$(".gobackerror").click(function() {
		history.back();
	});
	$("#suggestions li span").tooltip();
};

$(document).ready(window.init);
