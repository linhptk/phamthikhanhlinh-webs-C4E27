from pymongo import MongoClient

mongo_uri="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db_mlab=client.c4e

river_collection=db_mlab["data_river_collection"]
# dict_river_collection=river_collection.find()
# print(dict_river_collection)