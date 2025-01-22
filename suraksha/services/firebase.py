import pyrebase
from dotenv import load_dotenv

load_dotenv()

from suraksha.config import config


firebase = pyrebase.initialize_app(config.FIREBASE_CONFIG)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()
