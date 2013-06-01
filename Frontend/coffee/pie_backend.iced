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

class PieBackend
  constructor:(@bottles) ->

  byPrice: (bottles, label) ->
    label: label,
    value: sum(_.map(bottles, (bottle) -> bottle.num_bottles * priceOf bottle))
    
  byNumBottles: (bottles, label) ->
    label: label,
    value: bottles.length

  _render: (partitions, groupBy = @byPrice) ->
    _.map(partitions, groupBy)

  cellar: (groupBy) ->
    partitions = _.groupBy(@bottles, (bottle) -> bottle.cellar.name)
    @_render(partitions, groupBy)
  
  wine: (groupBy) ->
    partitions = _.groupBy(@bottles, (bottle) -> bottle.wine.name)
    @_render(partitions, groupBy)

  winery: (groupBy) ->
    getWineryName = (bottle) ->
      if bottle.wine.winery
        bottle.wine.winery.name
      else
        "None"

    partitions = _.groupBy(@bottles, getWineryName)
    @_render(partitions, groupBy)

  color: (groupBy) ->
    partitions = _.groupBy(@bottles, (bottle) -> bottle.wine.color)
    @_render(partitions, groupBy)

  type: (groupBy) ->
    partitions = _.groupBy(@bottles, (bottle) -> bottle.wine.wine_type)
    @_render(partitions, groupBy)

  raw: (partitionFunc, groupBy) ->
    partitions = _.groupBy(@bottles, partitionFunc)
    @_render(partitions, groupBy)

window.createPieBackend = (userId, callback) ->
  await window.backend.Bottle.get {"cellar__owner": userId, "limit": 0}, defer bottles
  callback new PieBackend bottles
