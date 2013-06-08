$ ->

  loadWineDataIntoUI = (wine)->
    $("#winename").val wine.name
    $("#year").val wine.vintage
    $("#alcoholcontent").val wine.alcohol_content
    $("#winetype").val wine.wine_type
    $("#wineryname").val wine.winery.name
    $("#retailprice").val wine.retail_price
    $("#winenamelabel").append wine.name
    if JSON.parse(wine.raw_data)
      JSONParser(JSON.parse wine.raw_data)
    else
      $(".json").remove()

  $("#valaddwine").click (event) ->
      $("#addwine").valreset()
      event.preventDefault()


      # Validation
      
      if $("#imagefile").val() and window.FileReader
        if $("#imagefile")[0].files[0].size / (1024 * 1024) > 10
          alert "That file is too big! Try another one"
          return


      name = $("#winename").vallength()
      year = $("#year").valvintageyear()
      alcohol = $("#alcoholcontent").valnumber()
      cellar = $("#cellar").valselect()
      type = $("#winetype").valselect()
      bottles = $("#numbottles").valnumber()
      winery = $("#wineryname").vallength()
      price = $("#retailprice").valnumber()
      if not name or not year or not alcohol or not cellar or not type or not bottles
        console.log("Error Condition")
        return

      # Loading stuff
      $("#loading").show()
      $("#valaddwine").addClass("disabled").html("Adding Wine...")

      # Create wine
      wine =
        name: name
        vintage: year
        alcohol_content: alcohol
        wine_type: type
        retail_price: (parseFloat price) or 0

      # Create/Get the winery, if necessary
      if winery
        await backend.Winery.getOrCreate {name: winery}, defer wineryObj
        wine.winery = {id: wineryObj.id}
      
      # Create/Get the wine
      await backend.Wine.getOrCreate wine, defer wineObj

      bottle =
        wine: {id: wineObj.id}
        cellar: {id: parseInt cellar}
        num_bottles: bottles

      # Create the bottle
      await backend.Bottle.create bottle, defer newbottle

      if $("#imagefile").val()
        await backend.uploadImage new FormData($("#upload-photo-form")[0]), newbottle.id, defer nothing

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
    $(".json").remove()
