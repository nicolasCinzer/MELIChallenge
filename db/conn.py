import os

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(os.environ["MONGO_URI"], server_api=ServerApi('1'))

db = client.challenge_db
collection_dnas = db['dnas']
