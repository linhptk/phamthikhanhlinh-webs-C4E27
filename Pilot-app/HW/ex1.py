from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)
db_ex1 = client.c4e
first_post = db_ex1["posts"]
linh_post = {
    "title": "Điều tuyệt nhất của chúng ta <3",
    "author":"PTKL",
    "content":"Cậu ấy của năm đó chính là cậu ấy tuyệt vời nhất. Nhưng tôi của mãi sau này mới là tôi tuyệt vời nhất. Giữa những con người tuyệt vời nhất của chúng tôi cách nhau một tuổi trẻ. Dù chạy thế nào cũng không thể thắng được thanh xuân.",

}
first_post.insert_one(linh_post)