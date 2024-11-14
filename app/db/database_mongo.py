import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv(verbose=True)
client = MongoClient(os.environ['MONGO_URI'])

db = client[os.environ['MONGO_DB_NAME']]
# members_collection = db['members_collection']
# _collection = db['menu']
# menu_collection = db['menu']