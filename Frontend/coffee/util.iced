window.Util =
  byId: (obj) -> obj.id
  flatMap: (list, fn) ->
    return _.reject _.map(list, fn), (elem) -> not elem
