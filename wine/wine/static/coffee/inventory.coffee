console.log "Coffeescript Compilation Works!"

$ ->

  $(".create-cellar-button").click ->
    name = $("#cellar-name").val()
    location = $("#cellar-location").val()
    lat = $("#cellar-latitude").val()
    lon = $("#cellar-longitude").val()
    point = undefined
    if lat and lon
      point =
        lat: parseFloat(lat)
        lon: parseFloat(lon)

    clicked = ->
      window.helpers.getMyCellars (cellars) ->
        window.helpers.getUserInfo window.userId, displayUserInfo
        renderCellars(cellars)

    helpers.createCellar(name, location, point, clicked)

  displayUserInfo = (userInfo) ->
    numCellars = userInfo.cellars.length
    $("#user-info").html "Hello #{userInfo.first_name}, you have #{numCellars} cellars."

  renderCellars = (cellars) ->
    # TODO: This should be using JST
    tableString = "<table><tr><td>Cellar Name</td><td>Cellar Location</td>"
    for cellar in cellars
      tableString += "<tr><td>#{cellar.name}</td><td>#{cellar.location}</td>"
    tableString += "</table>"
    $("#cellar-table").html(tableString)

  window.helpers.getUserInfo window.userId, displayUserInfo
  window.helpers.getMyCellars(renderCellars)
