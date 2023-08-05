import firebase_admin
import requests
from firebase_admin import credentials
from firebase_admin import firestore
import requests
import json

#firebase
cred = credentials.Certificate("C:/Users\zach\Desktop\Snazzy OTP\sAK.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
db_doc_name = "snazzy-keys"

# get all keys
keys = db.collection(db_doc_name)
res = keys.get()
for i in res:
    # delete key
    db.collection(db_doc_name).document(i.id).delete()
    