import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class FireBase:
    def __init__(self, token_file_path):
        self.token_file_path = token_file_path
        self.certificate = credentials.Certificate(self.token_file_path)
        firebase_admin.initialize_app(self.certificate)
        self.db = firestore.client()

    def get_collection(self, collection):
        return Collection(self.db.collection(collection))

class Collection:
    def __init__(self, collection):
        self.collection = collection
    
    def get_document(self, document):
        return self.collection.document(document).get().to_dict()
    
    def set_document(self, document, data):
        return self.collection.document(document).set(data)