console.log "Coffeescript Compilation Works!"
$ ->

  # Display Functions

  renderCellars = (cellars) ->
    helpers.template("cellar_table", {cellars:cellars}, $("#cellar-table"))
    updateButtonListener = ->
      $(".delete-cellar-button").click ->
        id = $(this).data("id")
        await window.helpers.deleteCellar id, defer nothing
        updatePage()
    setTimeout(updateButtonListener, 100)

  displayUserInfo = (userInfo) ->
    numCellars = userInfo.cellars.length
    $("#user-info").html "Hello #{userInfo.first_name}, you have #{numCellars} cellars."

  updatePage = ->
    await window.helpers.getMyCellars defer cellars
    await window.helpers.getUserInfo window.userId, defer userInfo
    displayUserInfo(userInfo)
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

    await helpers.createCellar(name, location, point) defer nothing
    updatePage()

  updatePage()
