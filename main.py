import auth


username = "Alaba"
password = "password123"
password2 = "password123"


auth.signup(username,password, password2)
auth.login(username, password)
