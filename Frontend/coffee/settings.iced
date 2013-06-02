$ ->
  $("#validatesettings").click (event) ->
      event.preventDefault()
      $("#settings").valreset()
      name = $("#name").vallength()
      email = $("#email").valemail()
      pass = $("#newpass").valnewpassword()

      await backend.updateUserAccount name, email, pass, defer response
      window.location="collection.html"
