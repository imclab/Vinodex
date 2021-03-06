window.cellsPerRow = ->
  width = $("#results").width()
  if width > 960 then 5
  else if width > 768 then 4
  else if width > 480 then 3
  else 2

window.isotopeResults = ->
  $("#results").isotope
    itemSelector: '.result'
    resizable: false
    layoutMode: 'cellsByRow'
    cellsByRow:
      columnWidth: $("#results").width() / cellsPerRow()
      rowHeight: 270
    getSortData:
      name: ($elem) -> $elem.find(".name").text()
      date: ($elem) -> parseInt $elem.data("timestamp")
      bottles: ($elem) -> parseInt $elem.find(".numbottles").text()
      retailPrice: ($elem) -> parseInt $elem.find(".retailPrice").text().replace("$","")
      alcoholcontent: ($elem) -> parseInt $elem.find(".alcoholcontent")
                                               .text()
                                               .replace("%", "")

  $("#results").mouseenter( ->
      $(window).resize()
      $('#results').isotope("reLayout")
  )

  $("#results").on("click", ".result", ->
      $(this).toggleClass("selected")
  )


addListeners = ->
  $("#add-wine-name-button").click (event) ->
    event.preventDefault()
    if selectedWine
      window.location = "/addwine.html##{selectedWine.id}"
    else
      wineName = $("#wine-name-input").val()
      window.location = "/addwine.html##{wineName}"

  $("#deleteconfirm").click (event) ->
    event.preventDefault()
    if $("#deletetext").val().trim() == "DELETE"
      $(".selected").each ->
        bottleId = $(@).data("id")
        backend.Bottle.delete bottleId, -> {}
      $("#results").isotope("remove",$(".selected"));
      $("#deletewine").modal "hide"
    else
      event.preventDefault()
      $("#deletetext").valerror()

  $("a[href='#uploadbarcode']").click (event) ->
      event.preventDefault()
      window.uploadMode = "barcode"
      $("#imageselector").click()

  $("a[href='#uploadlabel']").click (event) ->
      event.preventDefault()
      window.uploadMode = "label"
      $("#imageselector").click()

  $("#imageselector").change ->
      if window.uploadMode == "barcode"
        await backend.identifyBarcode new FormData($("#wine-vision-form")[0]), defer wines
      else
        await backend.identifyLabel new FormData($("#wine-vision-form")[0]), defer wines

      if not wines
        wines = []
      localStorage.setItem("visionResult", JSON.stringify wines)
      window.location = "autocompleteresults.html"

$ ->

  $("#sharelink").html("http://vinodex.us/print.html##{window.backend.userId}")
  addListeners()
  await
    backend.Bottle.get {cellar__owner: backend.userId, limit: 1000}, defer bottles
    backend.Cellar.get {owner: backend.userId}, defer cellars
  wineTypes = _.uniq Util.flatMap(bottles, (bottle) -> bottle.wine.wine_type)
  wineries = _.uniq(Util.flatMap(bottles, (bottle) -> bottle.wine.winery), false, Util.byId)
  await
    window.frontend.renderTemplate "collection_wines", {bottles: bottles}, defer collection
    window.frontend.renderTemplate "collection_nav",
      wineTypes: _.map(wineTypes, (type) -> type: type, pronounce: pronounce[type])
      cellars: cellars
      wineries: wineries, defer nav
  $("#results").html(collection)
  $("#collection-nav-list").html(nav)
  window.isotopeResults()
  $(".pronounciation").tooltip()
