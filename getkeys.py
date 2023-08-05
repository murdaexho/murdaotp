import firebase_admin
import requests
from firebase_admin import credentials
from firebase_admin import firestore
import requests
import json
import os

#firebase
cred = credentials.Certificate(os.getcwd() + "\\sAK.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
db_doc_name = "floop-keys"

# Get the keys from the database
keys = db.collection(db_doc_name)
res = keys.get()
for i in res:
    print(i.id)

# write to file
with open('keys.txt', 'w') as f:
    for i in res:
        f.write(i.id + "\n")