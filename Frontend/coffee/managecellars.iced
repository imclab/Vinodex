$ ->
  refreshCellars = ->
    await backend.Cellar.get {owner: backend.userId}, defer cellars
    await frontend.renderTemplate "manage_cellars_table", {cellars: cellars}, defer html
    $("#cellars-table-body").html(html)
    $(".editcellar-button").click ->
      window.selectedCellar = parseInt($(@).data "cellar-id")

  $("#create-cellar-button").click (event) ->
    event.preventDefault()
    name = $("#create-cellar-name").val()
    await backend.Cellar.create {owner: backend.profileUri, name: name}, defer nothing
    refreshCellars()

  $("#deleteconfirm").click (event) ->
    event.preventDefault()
    if $("#deletetext").val().trim() == "DELETE"
      await backend.Cellar.delete window.selectedCellar, defer nothing
      refreshCellars()
      $("#deletecellar").modal "hide"
    else
      $("#deletetext").valerror()

  $("#save-cellar").click (event) ->
    cellarName = $("#cellarname").val()
    await backend.Cellar.update window.selectedCellar, {name: cellarName}, defer nothing
    refreshCellars()

  refreshCellars()

