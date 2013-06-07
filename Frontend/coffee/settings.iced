$ ->
  $("#validatesettings").click (event) ->
      event.preventDefault()
      $("#settings").valreset()
      name = $("#name").vallength()
      email = $("#email").valemail()
      pass = $("#newpass").valnewpassword()

	  if not name or not email or not pass?
        console.log("Error Condition")
        return

	  # Loading stuff
	  $("#loading").show()
	  $("#validatesettings").addClass("disabled").html("Saving Changes...")

      await backend.updateUserAccount name, email, pass, defer response
      window.location="collection.html"

  $("#deleteacctconfirm").click (event) ->
    event.preventDefault()
    if $("#deleteconfirmtext").val() == "DELETE"
      await backend.deleteUserAccount defer response
      window.location="index.html"
