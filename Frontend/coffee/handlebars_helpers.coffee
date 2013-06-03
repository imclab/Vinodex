hyphenate = (str) ->
  str.split(" ").join "-"

toSeconds = (date) ->
  (new Date(date)).valueOf()

Handlebars.registerHelper "hyphenate", hyphenate
Handlebars.registerHelper "toSeconds", toSeconds
