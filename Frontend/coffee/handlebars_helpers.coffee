window.hyphenate = (str) ->
  str.replace(/[\ \.]/g,'-')

toSeconds = (date) ->
  (new Date(date)).valueOf()

Handlebars.registerHelper "hyphenate", hyphenate
Handlebars.registerHelper "toSeconds", toSeconds
