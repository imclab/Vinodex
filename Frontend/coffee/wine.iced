$ ->

  window.bottleId = parseInt window.location.hash.substr(1)
  if not bottleId
    window.location = "/collection.html"

  $("#deleteconfirm").click (event) ->
    event.preventDefault()
    await backend.Bottle.delete bottleId, defer nothing
    window.location = "/collection.html"

  renderPage = ->
    $(".templateContent").remove()
    await
      backend.Bottle.getById bottleId, defer bottle
      backend.Cellar.get {owner: backend.userId}, defer cellars
    await frontend.renderTemplate "wine", {bottle: bottle, cellars: cellars}, defer html
    $("#deletewine").before html

    $("#valaddwine").click (event) ->
        event.preventDefault()
        name = $("#winename").vallength()
        year = $("#year").valvintageyear()
        alcohol = $("#alcoholcontent").vallength()
        cellar = $("#cellar").valselect()
        type = $("#winetype").valselect()
        bottles = $("#numbottles").vallength()
        wineryName = $("#wineryname").val()
        price = $("#retailprice").val()
        if not name or not year or not alcohol or not cellar or not type or not bottles
          console.log("Error Condition")
          return
        await backend.Winery.getOrCreate {name: wineryName}, defer winery
        _wine =
          name: name
          vintage: year
          alcohol_content: alcohol
          wine_type: type
          retail_price: parseFloat price
          winery: winery
        await backend.Wine.getOrCreate _wine, defer wine

        _bottle =
          wine: "/api/v1/wine/#{wine.id}/"
          cellar: "/api/v1/cellar/#{bottle.cellar.id}/"
          num_bottles: bottles

        await backend.Bottle.update bottle.id, _bottle, defer nothing
        $("#editwine").modal "hide"
        renderPage()

  renderPage()
