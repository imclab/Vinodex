$ ->
  await backend.Cellar.get {owner__id: backend.userId}, defer cellars
  await frontend.renderTemplate "manage_cellars_table", {cellars: cellars}, defer html
  $("#cellars-table-body").html(html)
