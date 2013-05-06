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

    helpers.createCellar(name, location, point)

  displayUserInfo = (userInfo) ->
    alert "Hello #{userInfo.first_name} #{userInfo.last_name}"
    numCellars = userInfo.cellars.length
    $("#cellar-text").html "You have #{numCellars} cellars"

  window.helpers.getUserInfo window.userId, displayUserInfo
