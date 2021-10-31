from django.shortcuts import render
import firebase_admin
from firebase_admin import db

# Create your views here.

firebase_cred_obj = firebase_admin.credentials.Certificate('auth.json')
default_app = firebase_admin.initialize_app(firebase_cred_obj, {'databaseURL':databaseURL})

ref = db.reference("/")

import json
with open("book_info.json", "r") as f:
	file_contents = json.load(f)
ref.set(file_contents)
