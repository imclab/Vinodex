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

  helpers.createCellar = (name, location, point, callback) ->
    cellar =
      "owner": {pk: window.userId}
      "name": name
      "location": location
      # "point": point or undefined

    $.ajax
      url: "/api/v1/cellar/",
      contentType: "application/json"
      type: "POST"
      data: JSON.stringify(cellar)
      dataType: "text/json"
      processData: false
      success: callback
    

  window.helpers = helpers
