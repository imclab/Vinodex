$ ->
  bottle_ids = JSON.parse($.cookie 'toprint')
  bottles = []
  await
    if not bottle_ids.length
      backend.Bottle.get cellar__owner: backend.userId, defer bottles
    else
      backend.Bottle.getByIds bottle_ids.join(";"), defer bottles

    backend.Profile.getById backend.userId, defer user

  await frontend.renderTemplate "print", bottles: bottles, name: user.name, defer html
  $("body").html(html)
  window.print()
