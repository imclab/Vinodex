$ ->
  refreshCellars = ->
    await backend.Cellar.get {owner_id: backend.userId}, defer cellars
    await frontend.renderTemplate "manage_cellars_table", {cellars: cellars}, defer html
    $("#cellars-table-body").html(html)

  $("#create-cellar-button").click (event) ->
    event.preventDefault()
    name = $("#create-cellar-name").val()
    await backend.Cellar.create {owner: backend.profileUri, name: name}, defer nothing
    refreshCellars()

  refreshCellars()

