# If the user is already logged in, then just redirect to the inventory
if window.backend.userIsLoggedIn()
  window.location = "collection.html"
