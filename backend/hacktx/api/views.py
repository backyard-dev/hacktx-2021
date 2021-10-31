from os import name
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from firebase_admin import firestore, credentials, auth
import firebase_admin
from firebase_admin import db

cred = credentials.Certificate('./auth.json')
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()


@api_view(['GET', 'POST'])
def signup(request):
    print(request)
    email = request.data['email']
    password = request.data['password']
    print('Password: ' + str(password))
    print('Email: ' + str(email))
    try:
        user = auth.create_user(email=email, password=password)
        token = auth.create_custom_token(user.uid)
        return Response(token, status=status.HTTP_200_OK)
    except:
        return Response('error', status=status.HTTP_400_BAD_REQUEST)
