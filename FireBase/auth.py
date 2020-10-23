import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyDHD-nx07TdehXyMYFu4912JjBoKAAHAdA",
    'authDomain': "test-db-288e8.firebaseapp.com",
    'databaseURL': "https://test-db-288e8.firebaseio.com",
    'projectId': "test-db-288e8",
    'storageBucket': "test-db-288e8.appspot.com",
    'messagingSenderId': "910949626140",
    'appId': "1:910949626140:web:e0298df55f26c3a79dcad9"
}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

# Login
# email = input("Enter your email\n")
# password = input("Enter your password\n")

# try:  
#     auth.sign_in_with_email_and_password(email, password)
#     print("Signed in Succesfully")
# except:
#     print("Invalid User or password")

Sign Up
email = input("Enter your email\n")
password = input("Enter your password\n")
confirm_password = input("Confirm Password\n")

if password == confirm_password:
    try:
        auth.create_user_with_email_and_password(email, password)
        print("Success")
    except:
        print("Email already exists!")


