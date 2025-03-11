from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()


MONGO_URI = os.getenv("DATABASE_URL")
print(MONGO_URI)

conn = MongoClient(MONGO_URI)