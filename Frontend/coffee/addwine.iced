$ ->

  loadWineDataIntoUI = (wine)->
    $("#winename").val wine.name
    $("#year").val wine.vintage
    $("#alcoholcontent").val wine.alcohol_content
    $("#winetype").val wine.wine_type
    $("#wineryname").val wine.winery.name
    $("#retailprice").val wine.retail_price

  $("#valaddwine").click (event) ->
      $("#addwine").valreset()
      event.preventDefault()

      # Validation
      
      name = $("#winename").vallength()
      year = $("#year").valvintageyear()
      alcohol = $("#alcoholcontent").vallength()
      cellar = $("#cellar").valselect()
      type = $("#winetype").valselect()
      bottles = $("#numbottles").vallength()
      winery = $("#wineryname").val()
      price = $("#retailprice").val()
      if not name or not year or not alcohol or not cellar or not type or not bottles
        console.log("Error Condition")
        return

      # Create wine
      wine =
        name: name
        vintage: year
        alcohol_content: alcohol
        type: type
        retail_price: parseFloat price

      # If the user wants to associate a winery with the wine,
      # look for a winery with the same name, and use that instead
      if winery

        # Check if the winery exists
        await backend.Winery.get {name: winery, limit: 1}, defer matchingWineries

        if matchingWineries.length
          # Winery already exists with this name, return it
          winery_id = matchingWineries[0].id
          wine.winery = "/api/v1/winery/#{winery_id}/"
        else
          # No such winery exists, create it
          await backend.Winery.create {name: winery}, defer winery
          wine.winery = "/api/v1/winery/#{winery.id}/"

      wine = undefined
      
      # Check if the wine exists
      await backend.Wine.get wine, defer wines
      if wines.length
        wine = wines[0]
      else
        await backend.Wine.create wine, defer wine

      bottle =
        wine: "/api/v1/wine/#{wine.id}/"
        cellar: "/api/v1/cellar/#{cellar}/"

      # Create the bottle
      await backend.Bottle.create bottle , defer nothing

      # Go home
      window.location = "/collection.html"


  # Load the cellars into the form
  await window.backend.Cellar.get {owner: window.backend.userId}, defer cellars
  await frontend.renderTemplate "addwine_cellars", {cellars: cellars}, defer html
  $("#cellar").html(html)

  wineId = parseInt window.location.hash.substr(1)
  if wineId
    await backend.Wine.getById wineId, defer wine
    loadWineDataIntoUI wine
  else
    $("#winename").val(window.location.hash.substr(1))
