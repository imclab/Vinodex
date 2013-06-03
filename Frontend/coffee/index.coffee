# If the user is already logged in, then just redirect to the inventory
if backend.userIsLoggedIn()
  window.location = "collection.html"
