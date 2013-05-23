$ ->
  bottleId = parseInt window.location.hash.substr(1)
  if not bottleId
    window.location = "/collection.html"
  await backend.Bottle.getById bottleId, defer bottle
  await frontend.renderTemplate "bottle", bottle, defer html
  $("#deletewine").before html
