def sign_in(username, password):
    valid_username = "admin"
    valid_password = "password"

    if username == valid_username and password == valid_password:
        return True
    else:
        return False