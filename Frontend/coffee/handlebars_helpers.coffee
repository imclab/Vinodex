window.hyphenate = (str) ->
  str.replace(/[\ \.\']/g,'-')

toSeconds = (date) ->
  (new Date(date)).valueOf()

prettyDate = (date) ->
  (new Date(date)).toLocaleDateString()

renderRating = (rating) ->
  if not rating
    rating = 0
  str = ""
  i = 0
  while i < rating and i < 5
    str += '<i class="icon-star"></i>'
    i += 1
  while i < 5
    str += '<i class="icon-star-empty"></i>'
    i += 1
  str

Handlebars.registerHelper "hyphenate", hyphenate
Handlebars.registerHelper "toSeconds", toSeconds
Handlebars.registerHelper "prettyDate", prettyDate
Handlebars.registerHelper "renderRating", renderRating
