window.cellsPerRow = ->
  width = $("#results").width()
  if width > 960 then 5
  if width > 768 then 4
  if width > 480 then 3
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
    wineName = $("#wine-name-input").val()
    window.location = "/addwine.html##{wineName}"

  $("#deleteconfirm").click (event) ->
    $(".selected").each ->
      bottleId = $(@).data("id")
      backend.Bottle.delete bottleId, -> {}
    $(".selected").remove()

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

      localStorage.setItem("visionResult", JSON.stringify wines)
      window.location = "autocompleteresults.html"

$ ->

  addListeners()
  await
    backend.Bottle.get {cellar__owner: backend.userId, limit: 1000}, defer bottles
  wineTypes = _.uniq Util.flatMap(bottles, (bottle) -> bottle.wine.wine_type)
  wineries = _.uniq(Util.flatMap(bottles, (bottle) -> bottle.wine.winery), false, Util.byId)
  cellars = _.uniq _.pluck(bottles, "cellar"), false, Util.byId
  await
    window.frontend.renderTemplate "collection_wines", {bottles: bottles}, defer collection
    window.frontend.renderTemplate "collection_nav",
      wineTypes: wineTypes
      cellars: cellars
      wineries: wineries, defer nav
  $("#results").html(collection)
  $("#collection-nav-list").html(nav)
  window.isotopeResults()
