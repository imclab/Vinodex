window.hyphenate = (str) ->
  str.replace(/[\ \.\']/g,'-')

toSeconds = (date) ->
  (new Date(date)).valueOf()

prettyDate = (date) ->
  (new Date(date)).toLocaleDateString()

Handlebars.registerHelper "hyphenate", hyphenate
Handlebars.registerHelper "toSeconds", toSeconds
Handlebars.registerHelper "prettyDate", prettyDate
