  helpers = {}

  helpers.handleApiResponseForOneElement = (response, callback) ->
    objects = response.objects
    if objects.length == 0
      throw "No Object was returned"
    else if objects.length > 2
      console.warn "Only one object was queried for, but #{response.objects.length} objects\
                    were returned"
      console.warn "Only using the first object"
    callback(objects[0])


  helpers.getUserInfo = (userId, callback) ->
    $.get("/api/v1/profile", {"user_id": userId}, (response) ->
      helpers.handleApiResponseForOneElement(response, callback))

  helpers.getMyCellars = (callback) ->
    $.get("/api/v1/cellar", {"owner_id": userId, limit: 0}, (response) ->
      callback(response.objects))

  helpers.post = (uri, data, callback) ->
    $.ajax
      url: uri
      contentType: "application/json"
      type: "POST"
      data: JSON.stringify(data)
      dataType: "text/json"
      processData: false
      complete: callback

  helpers.templateNameToUrl = (templateName) ->
    "/static/jst/#{templateName}.jst"

  helpers.template = (templateName, data, $div) ->
    templateUrl = helpers.templateNameToUrl templateName
    templateFunction = (templateText) -> $div.html(_.template(templateText)(data))
    $.get(templateUrl, {}, templateFunction, "text")


  helpers.createCellar = (name, location, point, callback) ->
    cellar =
      "owner": {pk: window.userId}
      "name": name
      "location": location
      "point": point or undefined

    helpers.post("/api/v1/cellar/", cellar, callback)

  window.helpers = helpers
