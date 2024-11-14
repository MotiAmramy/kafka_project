import os
from dotenv import load_dotenv
from pymongo import MongoClient



load_dotenv(verbose=True)
client = MongoClient(os.environ['MONGO_URI'])

db = client[os.environ['MONGO_DB_NAME']]
messages_collection = db[os.environ['MONGO_COLLECTION_NAME_MESSAGE_ALL']]
