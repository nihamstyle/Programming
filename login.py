# authentication.py

def sign_in(password, username):

    with open('credentials.txt', 'r') as file:
        stored_username, stored_password = file.read().split(',')
        if username == stored_username and password == stored_password:
            return True
    return False