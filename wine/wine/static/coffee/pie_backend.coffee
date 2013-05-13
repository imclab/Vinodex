BOTTLE_URI = "http://localhost:8000/api/v1/bottle?format=json"

priceOf = (bottle) ->
  if bottle.price
    bottle.price
  else if bottle.wine.retail_price
    bottle.wine.retail_price
  else if bottle.wine.min_price and bottle.wine.max_price
    (bottle.wine.min_price + bottle.wine.max_price) / 2
  else
    bottle.max_price or bottle.min_price or 0

plus = (a, b) -> a + b

sum = (list) ->
 _.reduce(list, plus, 0)

__createBackend = (bottles) ->
  bottles: bottles

  byPrice: (bottles, label) ->
    label: label,
    value: sum(_.map(bottles, (bottle) -> priceOf bottle))
    
  byNumBottles: (bottles, label) ->
    label: label,
    value: bottles.length

  _render: (partitions, groupBy = this.byPrice) ->
    _.map(partitions, groupBy)

  cellar: (groupBy) ->
    partitions = _.groupBy(this.bottles, (bottle) -> bottle.cellar.name)
    this._render(partitions, groupBy)
  
  wine: (groupBy) ->
    partitions = _.groupBy(this.bottles, (bottle) -> bottle.wine.name)
    this._render(partitions, groupBy)

  winery: (groupBy) ->
    getWineryName = (bottle) ->
      if bottle.wine.winery
        bottle.wine.winery.name
      else
        "None"

    partitions = _.groupBy(this.bottles, getWineryName)
    this._render(partitions, groupBy)

  color: (groupBy) ->
    partitions = _.groupBy(this.bottles, (bottle) -> bottle.wine.color)
    this._render(partitions, groupBy)

  type: (groupBy) ->
    partitions = _.groupBy(this.bottles, (bottle) -> bottle.wine.wine_type)
    this._render(partitions, groupBy)

  raw: (partitionFunc, groupBy) ->
    partitions = _.groupBy(this.bottles, partitionFunc)
    this._render(partitions, groupBy)

window.createBackend = (userId, notifyFunc = () -> null) ->
  await $.get BOTTLE_URI, {"cellar__owner": userId, "limit": 0}, defer response

  bottles = response.objects
  window.backend = __createBackend(bottles)

  notifyFunc(window.backend)
