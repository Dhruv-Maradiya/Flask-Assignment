from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# MongoDB connection setup
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["ecommerce"]

# Export collections
products_collection = db["products"]

# Ensure indexes for efficient querying
def setup_indexes():
    products_collection.create_index("name")
    products_collection.create_index("category")
