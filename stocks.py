import pymongo
from pymongo import MongoClient

client = MongoClient(
  "mongodb+srv://admin:Hlw7V8CtNJ0hXsgk@cluster0.jrxen8d.mongodb.net/?retryWrites=true&w=majority"
)

#Make sure to replace this with the name of the database, which you can find in this lab's readme!
db = client['DATABASE-NAME'] 

# Note: "prices" is the name of the collection where all the data is stored
collection = db.prices       


# write your queries here (#1)
all_stocks = list(collection.find({}))
print(all_stocks)
