$ ->
  await backend.Sommelier.get limit: 1000, defer sommelierData
  console.log sommelierData
  byPairs = _.groupBy sommelierData, "pairing"
  byWines = _.groupBy sommelierData, "wine_type"
  foods = _.keys byPairs
  foods.sort()
  await frontend.renderTemplate "select_meal_dropdown", meals: foods, defer html
  $("#meal-select-form").append html
  $("select.span3").change ->
    pairs = byPairs[$(@).val()]
    wineTypes = _.uniq( _.pluck(pairs, "wine_type"))

    await backend.Wine.get
      wine_type__in: wineTypes.join ","
      limit: 10
      order: 'rand', defer wines

    wines = _.map wines, (wine) ->
      wine.description = byWines[wine.wine_type][0].description
      wine

    await
      frontend.renderTemplate "sommelier_wines", wines: wines, defer wineHtml
      frontend.renderTemplate "sommelier_winetypes", pairs: pairs, defer wineTypeHtml
    $("#wines").html wineHtml
    $("#suggestions").html wineTypeHtml
    $(".winetype").tooltip()

