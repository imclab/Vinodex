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
		backend.createUserAccount(name, email, pass, function(){
			window.location = "collection.html";
		}, function(){console.log("Account Creation Failed");});
	});
	$("#validatepasschange").click(function(event) {
		event.preventDefault();
		$("#passchange").valreset();
		var pass = $("#passchangepass").valpassword();
	});
	$("#forgotpassval").click(function(event) {
		$("#login").valreset();
		var email = $("#forgotemail").valemail();
	});
};

$(document).ready(window.init);
