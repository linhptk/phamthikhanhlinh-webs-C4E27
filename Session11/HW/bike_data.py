from pymongo import MongoClient
from bson.objectid import ObjectId

# 1. Connect mongodb
mongo_uri = "mongodb+srv://admin:admin@pilot-app-c2zfj.mongodb.net/test?retryWrites=true"
client = MongoClient(mongo_uri)

# 2. Get/create database
bike_database = client.hw_session10

# 3. Get/Create collection
bike_collection = bike_database["bike_data"]
