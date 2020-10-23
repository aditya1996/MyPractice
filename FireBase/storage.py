import pyrebase
import urllib

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

storage = firebase.storage()

### Uploading a File to FireBase Storage

# filename = input("Enter the name of the file")
# cloudfilename = input("Enter the name of the file you want to be named in cloud") # you can also generate path as gibberish/textfiles/1.txt in FireBase Storage

# storage.child(cloudfilename).put(filename)

# print(storage.child(cloudfilename).get_url(None))

# -----------------------------------------------------------------------------------------

### Downloading a file from FireBase Storage

# cloudfilename = input("Enter the name of the file you want to download from cloud")
# storage.child(cloudfilename).download("","downloaded.txt")

# -----------------------------------------------------------------------------------------

### Reading file

cloudfilename = input("Enter the name of the file you want to read from cloud\n")
url = storage.child(cloudfilename).get_url(None)

f = urllib.request.urlopen(url).read()
print(f)