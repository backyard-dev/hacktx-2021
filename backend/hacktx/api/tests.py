from django.test import TestCase

# Create your tests here.

from firebase_db import FireBase

db = FireBase('credentials/firebase-key.json')
col = db.get_collection('testing')

doc = col.get_document('testing_doc')
print(doc)

doc['dlz'] = 'great'
col.set_document('testing_doc', doc)

doc = col.get_document('testing_doc')
print(doc)