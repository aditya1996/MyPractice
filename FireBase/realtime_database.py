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

db = firebase.database()

#### DataBase

# data = {'age' : 25, 'address' : "New York", 'employed' : True, 'name' : "Mark"}
# db.push(data)

# db.child("people").push(data)

# db.child("notes").child("Male").push(data)

# -----------------------------------------------------------------------------------------

#### Having your own unique ID

# data = {'age' : 27, 'address' : "ajamgarh", 'employed' : True, 'name' : "Pappu"}

# db.child("people").child("myownid").set(data)

# -----------------------------------------------------------------------------------------

#### Updating Entries | Changing name from "Pappu" to "Kumar"

# db.child("people").child("myownid").update({"name" : "Kumar"}) # || if name field is not there, it will create one ||

# -----------------------------------------------------------------------------------------

#### Updating age of person without knowing the unique id

# people = db.child("people").get()

# for i in people.each():

#     if i.val()["name"] == "Mark":
#         db.child("people").child(i.key()).update({'age' : 23})

# -----------------------------------------------------------------------------------------

#### Delete

# db.child("people").child("person").child("age").remove()

# db.child("people").child("person").remove()

# people = db.child("people").get()

# for i in people.each():

#     if i.val()["name"] == "Kumar":
#         db.child("people").child(i.key()).remove()

# -----------------------------------------------------------------------------------------

#### Read

# people = db.child("people").child("person").get()
# print(people.val())

# people = db.child("people").order_by_child("name").equal_to("Aditya").get()

# for i in people.each():
#     print(i.val())

# people = db.child("people").order_by_child("age").start_at(20).end_at(25).get()

# for i in people.each():
#     print(i.val())

# people = db.child("people").order_by_child("employed").equal_to(True).get()

# for i in people.each():
#     print(i.val())

# people = db.child("people").order_by_child("employed").equal_to(True).limit_to_first(1).get() ## || limit to first = get the 1st result from top (similarly you can use limit_to_last)

# for i in people.each():
#     print(i.val())

# people = db.child("people").order_by_child("employed").equal_to(True).get() 

# for i in people.each():
#     print(i.val()["name"])

