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
		/**
		* validation functions return null on invalid input nowm
		* in addition to putting errors on the fields
		* return the actual values on valid input
		*/
		backend.login(email, pass, function(){
			window.location = "collection.html";
		}, function(){console.log("Login Failed");});
		// change ^ so if any of the values are null, login doesn't take place?
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
		if(name !== null && email !== null && pass !== null) {
			$(this).addClass("disabled").html("Signing Up...");
			$(this).next().show().children(".bar").width("100%");
		}
		backend.createUserAccount(name, email, pass, function(){
			window.location = "collection.html";
		}, function(){
			console.log("Account Creation Failed");
			$("#validatesignup").removeClass("disabled").html("Sign Up");
			$("#validatesignup").next().hide().children(".bar").width("0%");
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
		var removereason = $("#removereason").html();
		var removequantity = $("#removequantity").valnumber();
	});
	$("#validatesettings").click(function(event) {
		event.preventDefault();
		$("#settings").valreset();
		var name = $("#name").vallength();
		var email = $("#email").valemail();
		var pass = $("#newpass").valpassword();
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
};

$(document).ready(window.init);
