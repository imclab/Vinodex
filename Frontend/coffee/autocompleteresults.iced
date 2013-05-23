$ ->
  wines = JSON.parse(localStorage.getItem "visionResult")
  await frontend.renderTemplate "autocompleteresults", {wines: wines}, defer html
  $("#autocompleteresults").html(html)
