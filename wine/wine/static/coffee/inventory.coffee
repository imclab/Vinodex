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
    helpers.template("cellar_table", {cellars:cellars}, $("#cellar-table"))

  window.helpers.getUserInfo window.userId, displayUserInfo
  window.helpers.getMyCellars(renderCellars)
