class Frontend
  renderTemplate: (templateName, data, callback) ->
    await $.get "/jst/#{templateName}.jst", defer template
    html = Mustache.render template, data
    callback html

window.frontend = new Frontend
