from pymongo import MongoClient
from bson.objectid import ObjectId

# 1. Connect mongodb
mongo_uri = "mongodb+srv://admin:admin@pilot-app-c2zfj.mongodb.net/test?retryWrites=true"
client = MongoClient(mongo_uri)

# 2. Get/create database
db_demo = client.test_database

# 3. Get/Create collection
first_collection = db_demo["my_collection"]

# 4. Create document
# game_document = {
#     "title":"FO4",
#     "description":"Football Game",
# }

# # 5. Insert document
# first_collection.insert_one(game_document)

# 6. READ
# 6.1 READ ALL
# all_documents = first_collection.find()
# print(all_documents)
# for document in all_documents:
#     print(document["title"])

# 6.2 Read one
# one_document = first_collection.find_one({"title":"FO4"})
# print(one_document)

# 7. DELETE
# delete_document = first_collection.find_one({"_id":ObjectId("5c979aa97094bc0968ac2d4d")})
# print(delete_document)
# if delete_document is not None:
#     first_collection.delete_one(delete_document)
#     print("Deleted Complete!")
# else:
#     print("Not found")

# 8.UPDATE
# 8.1 Tim
update_document = first_collection.find_one({"_id":ObjectId("5c979d077094bc0f78ed9aa9")})
new_value = {"$set":{"title":"KHONG BIET"}}
first_collection.update_one(update_document, new_value)