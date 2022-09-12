# pymongo 尝试
import pymongo
import datetime

client = pymongo.MongoClient('localhost', 27017)
db = client['test-database']

collection = db.test_collection
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()
        }
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

one = posts.find_one()
print(one)

for post in posts.find():
    print(post)

