$ ->

  $("#forgotpassval").click (event) ->
    event.preventDefault()

    email = $("#forgotemail").val()

    await backend.sendForgotPasswordEmail email, defer response
    if response.message == "success"
      window.location = "/forgotpasswordsuccessful.html"
    else
      window.location = "/forgotpasswordnotfound.html"
