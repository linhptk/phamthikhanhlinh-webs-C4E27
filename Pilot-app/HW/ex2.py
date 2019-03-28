from pymongo import MongoClient
from matplotlib import pyplot
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

all_customer = list(customer_collection.find())
# print(all_customer)
for customer in all_customer:
    if customer["ref"] == "events":
        events = events + 1
    elif customer["ref"] == "wom":
        wom = wom + 1
    elif customer["ref"] ==  "ads":
        ads = ads + 1
print("events:", events)
print("ads:", ads)
print("wom", wom)
# 1. Prepare data
ref_counts = ["events","ads","wom"]
# 2 Prepare labels
ref_name = ["events","advertisements","word of mouth"]
# 3. Draw pie
pyplot.pie(ref_counts,labels=ref_name, autopct="%1.f%%", shadow=True, explode=[0,0,0.1])
pyplot.axis("equal")
pyplot.title("Bieu do ex2")

# 4. Show
pyplot.show()


