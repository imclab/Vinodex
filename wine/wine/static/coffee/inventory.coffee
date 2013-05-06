console.log "Coffeescript Compilation Works!"

$ ->

  # Display Functions

  renderCellars = (cellars) ->
    helpers.template("cellar_table", {cellars:cellars}, $("#cellar-table"))
    updateButtonListener = ->
      $(".delete-cellar-button").click ->
        id = $(this).data("id")
        window.helpers.deleteCellar(id, updatePage)
        updatePage()
    setTimeout(updateButtonListener, 100)

  displayUserInfo = (userInfo) ->
    numCellars = userInfo.cellars.length
    $("#user-info").html "Hello #{userInfo.first_name}, you have #{numCellars} cellars."

  updatePage = ->
    window.helpers.getMyCellars (cellars) ->
      window.helpers.getUserInfo window.userId, displayUserInfo
      renderCellars(cellars)

  # Interactions


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

    helpers.createCellar(name, location, point, updatePage)

  updatePage()
