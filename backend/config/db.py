from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

conn = MongoClient(os.getenv("MONGO_URL"))
