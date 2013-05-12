BOTTLE_URI = "http://localhost:8000/api/v1/bottle?format=json"

__createBackend = (bottles) ->
  bottles: bottles

  _render: (partitions) ->

    plus = (a, b) -> a + b
    
    sum = (list) ->
     _.reduce(list, plus, 0)
    
    reduce = (label, values) ->
      label: sum(values)

  cellar: (func) ->
    partitions = _.groupBy(this.bottles, "cellar.name")
    this._render(partitions)
  
  wine: (func) ->
    partitions = _.groupBy(this.bottles, "wine.name")
    this._render(partitions)

  winery: (func) ->
    partitions = _.groupBy(this.bottles, "winery.name")
    this._render(partitions)

  color: (func) ->
    partitions = _.groupBy(this.bottles, "wine.color")
    this._render(partitions)

  type: (func) ->
    partitions = _.groupBy(this.bottles, "wine.type")

window.createBackend = (userId, notifyFunc = () -> null) ->
  await $.get BOTTLE_URI, {"cellar.owner": userId}, defer response

  bottles = response.objects
  window.backend = __createBackend(bottles)

  notifyFunc(window.backend)
