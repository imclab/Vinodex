class Resource
  constructor : (@api_endpoint_url, @backend) ->

  get: (filters = {}, callback, limit = 20) ->
    filters.limit = limit
    backend.get(@api_endpoint_url, filters, callback)

  delete: (id, callback) ->
    backend.delete("#{@api_endpoint_url}/#{id}", callback)

  create: (object = {}, callback) ->
    backend.post(@api_endpoint_url, object, callback)

  update: (id, options, callback) ->
    backend.put("#{@api_endpoint_url}/#{id}", options, callback)

class Backend
  constructor : (@server_url) ->
    @Bottle = new Resource("/api/v1/bottle/")
    @Cellar = new Resource("/api/v1/cellar/")
    @Winery = new Resource("/api/v1/winery/")
    @Wine = new Resource("/api/v1/wine/")
    @Annotation = new Resource("/api/v1/annotation/")
    @Sommeilier = new Resource("/api/v1/sommeilier/")

  handleApiResponseForOneElement: (response, callback) ->
    objects = response.objects
    if objects.length == 0
      throw "No Object was returned"
    else if objects.length > 2
      console.warn "Only one object was queried for, but #{response.objects.length} objects\
                    were returned"
      console.warn "Only using the first object"
    callback(objects[0])


  getUserInfo: (userId, callback) ->
    $.get("/api/v1/profile", {"user_id": userId}, (response) ->
      handleApiResponseForOneElement(response, callback))

  getMyCellars: (callback) ->
    $.get("/api/v1/cellar", {"owner_id": userId, limit: 0}, (response) ->
      callback(response.objects))

  get: (uri, data, callback) ->
    $.get(@server_url + uri, data, callback)

  post: (uri, data, callback) ->
    $.ajax
      url: uri
      contentType: "application/json"
      type: "POST"
      data: JSON.stringify(data)
      dataType: "jsonp"
      processData: false
      complete: callback

  put: (uri, data, callback) ->
    $.ajax
      url: uri
      contentType: "application/json"
      type: "PUT"
      data: JSON.stringify(data)
      dataType: "jsonp"
      processData: false
      complete: callback

# helpers.templateNameToUrl = (templateName) ->
#   "/static/jst/#{templateName}.jst"
# helpers.template = (templateName, data, $div) ->
#   templateUrl = helpers.templateNameToUrl templateName
#   templateFunction = (templateText) -> $div.html(_.template(templateText)(data))
#   $.get(templateUrl, {}, templateFunction, "text")

  delete: (uri,callback) ->
    $.ajax
      url: uri
      type: "DELETE"
      complete: callback
      dataType: "jsonp"

  createUserAccount: (name, email, password) ->
    account =
      "name": name
      "email": email
      "password": password

    await @.post "#{@server_url}/api/v1/profile/", account, defer user
    console.log(user)
    window.user = user
    $.cookie("user", user.id)


  createCellar: (name, location, point, callback) ->
    cellar =
      "owner": {pk: window.userId}
      "name": name
      "location": location
      "point": point or undefined

    @.post("/api/v1/cellar/", cellar, callback)

window.backend = new Backend("http://localhost:8000")
