from pymongo import MongoClient
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)
# Get databese
db_ex2 = client.c4e
# 3. Get/Create collection
customer_collection = db_ex2["customers"]
events = customer_collection.find({"ref":"events"})
ads = customer_collection.find({"ref":"ads"})
wom = customer_collection.find({"ref":"wom"})

events = 0
ads = 0
wom = 0

all_customer = customer_collection.find()
for customer in all_customer:
    if customer["ref"] == "events":
        events = events + 1
    if customer["ref"] == "wom":
        wom = wom + 1
    if customer ==  "ads":
        ads = ads + 1

from matplotlib import pyplot
# 1. Prepare data
# 2 Prepare labels
# 3. Draw pie
# 4. Show



