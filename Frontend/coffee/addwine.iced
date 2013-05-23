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
      wine =
        name: name
        vintage: year
        alcohol: alcohol
        type: type
        bottles: 1
        retail_price: parseFloat price

      if winery
        await backend.Winery.get {name: winery, limit: 1}, defer matchingWineries
        if matchingWineries.length
          winery_id = matchingWineries[0].id
          wine.winery_id = winery_id
        else
          await backend.Winery.create {name: winery}, defer winery
          wine.winery_id = winery.id
      else
      
      await backend.Wine.create wine, defer wine
      bottle =
        wine: "/api/v1/wine/#{wine.id}/"
        cellar: "/api/v1/cellar/#{cellar}/"
      await backend.Bottle.create bottle , defer nothing
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
