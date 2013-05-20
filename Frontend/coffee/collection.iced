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

byId = (obj) -> obj.id

flatMap = (list, fn) ->
  return _.reject _.map(list, fn), (elem) -> not elem

  

$ ->
  await
    backend.Bottle.get {cellar__owner: backend.userId, limit: 1000}, defer bottles
  wineTypes = _.uniq flatMap(bottles, (bottle) -> bottle.wine.wine_type)
  wineries = _.uniq flatMap(bottles, (bottle) -> bottle.wine.winery), false, byId
  cellars = _.uniq _.pluck(bottles, "cellar"), false, byId
  await
    window.frontend.renderTemplate "collection_wines", {bottles: bottles}, defer collection
    window.frontend.renderTemplate "collection_nav",
      wineTypes: wineTypes
      cellars: cellars
      wineries: wineries, defer nav
  $("#results").isotope("destroy")
  $("#results").html(collection)
  
  window.init()

  console.log("Cellars:")
  console.log(cellars)
  console.log("Bottles:")
  console.log(bottles)
  console.log("Wine Types")
  console.log(wineTypes)
  console.log("Wineries")
  console.log(wineries)

