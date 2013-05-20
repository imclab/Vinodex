$ ->

  $("#valaddwine").click (event) ->
      $("#addwine").valreset()
      event.preventDefault()
      name = $("#winename").vallength()
      year = $("#year").valvintageyear()
      alcohol = $("#alcoholcontent").vallength()
      cellar = $("#cellar").valselect()
      type = $("#winetype").valselect()
      bottles = $("#numbottles").vallength()
      if name or year or alcohol or cellar or type or bottles
        console.log("Error Condition")
        return
      nameVal = $("#winename").val()
      yearVal = $("#year").val()
      alcoholVal = $("#alcoholcontent").val()
      cellarVal = $("#cellar").val()
      typeVal = $("#winetype").val()
      priceVal = $("#retailprice").val()
      wineryVal = $("wineryname").val()
      winery_id = null
      if wineryVal
        await backend.Winery.get {name: winery, limit: 1}, defer matchingWineries
        if matchingWineries
          winery_id = matchingWineries[0].id
        else
          await backend.Winery.create{name: winery}, defer winery
          winery_id = winery.id

      window.backend.Wine.create
        name: nameVal
        vintage: yearVal
        alcohol: alcoholVal
        cellar: cellarVal
        type: typeVal
        winery: winery_id
        bottles: 1
        retail_price: priceVal
      , -> window.location="/collection.html"
      

  $("#winename").val(window.location.hash.substr(1))

  # Load the cellars into the form
  await window.backend.Cellar.get {owner: window.backend.userId}, defer cellars
  await frontend.renderTemplate "addwine_cellars", {cellars: cellars}, defer html
  $("#cellar").html(html)
