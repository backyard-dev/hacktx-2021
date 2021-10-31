from django.shortcuts import render
from firebase_admin import firestore, credentials
import firebase_admin

# Create your views here.

cred = credentials.Certificate('./auth.json')
firebase_admin.initialize_app(cred)

db = firestore.client()