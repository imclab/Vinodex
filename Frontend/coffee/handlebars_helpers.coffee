hyphenate: (str) ->
  str.split(" ").join "-"

Handlebars.registerHelper "hyphenate", hyphenate
