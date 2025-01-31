import os
import json
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app, auth
from google.cloud import firestore as google_firestore
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class FirebaseService:
    _instance = None
    _app = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FirebaseService, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
            
        # Firebase credentials
        cred_dict = {
            "type": "service_account",
            "project_id": os.getenv('FIREBASE_PROJECT_ID'),
            "private_key": os.getenv('FIREBASE_PRIVATE_KEY').replace('\\n', '\n'),
            "client_email": os.getenv('FIREBASE_CLIENT_EMAIL'),
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": f"https://www.googleapis.com/robot/v1/metadata/x509/{os.getenv('FIREBASE_CLIENT_EMAIL')}"
        }
            
        try:
            # Check if Firebase is already initialized
            self._app = firebase_admin.get_app()
            print("Firebase already initialized")
        except ValueError:
            try:
                print("Initializing Firebase...")
                print("Credential dictionary created")
                print(f"Project ID: {cred_dict['project_id']}")
                print(f"Client Email: {cred_dict['client_email']}")
                
                # Initialize Firebase with explicit credentials
                cred = credentials.Certificate(cred_dict)
                print("Credentials certificate created")
                
                self._app = initialize_app(cred)
                print("Firebase initialized successfully")
            except Exception as e:
                print(f"Error initializing Firebase: {str(e)}")
                raise
        
        try:
            # Initialize Firestore
            print("Initializing Firestore...")
            self.db = google_firestore.Client.from_service_account_info(cred_dict)
            print("Firestore initialized successfully")
            self._initialized = True
        except Exception as e:
            print(f"Error initializing Firestore: {str(e)}")
            raise

    async def verify_token(self, token):
        """
        Verifies Firebase auth token
        """
        try:
            if not token:
                raise ValueError("No token provided")
            decoded_token = auth.verify_id_token(token, app=self._app)
            return decoded_token
        except Exception as e:
            print(f"Error verifying token: {str(e)}")
            raise

    async def save_mindmap(self, user_id, mindmap_data):
        """
        Saves mind map to Firestore
        """
        try:
            if not user_id or not mindmap_data:
                raise ValueError("Missing required data")
                
            # Add timestamp and user_id
            mindmap_data['userId'] = user_id
            mindmap_data['createdAt'] = firestore.SERVER_TIMESTAMP
            
            # Save to Firestore
            doc_ref = self.db.collection('mindmaps').document()
            doc_ref.set(mindmap_data)
            
            return doc_ref.id
        except Exception as e:
            print(f"Error saving mindmap: {str(e)}")
            raise

    async def get_user_mindmaps(self, user_id):
        """
        Gets all mind maps for a user
        """
        try:
            if not user_id:
                raise ValueError("User ID is required")
                
            # Query Firestore
            docs = self.db.collection('mindmaps')\
                .where('userId', '==', user_id)\
                .stream()
            
            # Convert to list
            mindmaps = []
            for doc in docs:
                mindmap = doc.to_dict()
                mindmap['id'] = doc.id
                mindmaps.append(mindmap)
            
            return mindmaps
        except Exception as e:
            print(f"Error getting mindmaps: {str(e)}")
            raise

    async def delete_mindmap(self, user_id, mindmap_id):
        """
        Deletes a mind map
        """
        try:
            if not user_id or not mindmap_id:
                raise ValueError("Missing required parameters")
                
            # Check ownership
            doc_ref = self.db.collection('mindmaps').document(mindmap_id)
            doc = doc_ref.get()
            
            if not doc.exists:
                raise ValueError("Mind map not found")
                
            if doc.to_dict()['userId'] != user_id:
                raise ValueError("Unauthorized access")
            
            # Delete document
            doc_ref.delete()
            return True
        except Exception as e:
            print(f"Error deleting mindmap: {str(e)}")
            raise 