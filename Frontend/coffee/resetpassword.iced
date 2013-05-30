$ ->
  cipher = frontend.getHash()
  $("#validatepasschange").click (event) ->
    event.preventDefault()
    new_password = $("#passchangepass").val()
    await backend.resetPassword cipher, new_password, defer response
    if response.message == "success"
      window.location = "resetpasswordsuccess.html"
    else
      alert "Failed to reset password"
