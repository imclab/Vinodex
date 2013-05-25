window.JSONParser = function (json) {
	"use strict";
	function buildList(data, isSub) {
		var html = (isSub) ? "<div>" : ""; // wrap with div if true
		html += "<ul>";
		for (var item in data) {
			if(data.hasOwnProperty(item) && data[item] != "") {
				if (typeof (data[item]) === "object") { // array will return "object"
					html += "<li class=\"expand\"><span>" + item + "</span> {" + buildList(data[item], false) + "}"; // submenu exists, call recursively, no wrapping div
				} else {
					html += "<li><span>" + item + " : " + data[item] + "</span>"; // no submenu
				}
				html += "</li>";
			}
		}
		html += "</ul>";
		html += (isSub) ? "</div>" : "";
		return html;
	}

	$(".json").append(buildList(json, true));
	$(".json > div").addClass("expanded");
	$(".json").on("click", "li.expand", function (event) {
		event.stopPropagation();
		$(this).toggleClass("expanded");
	});
	$(".json").on("click", "li", function (event) {
		event.stopPropagation();
	});
};
