import pymongo
from pymongo import MongoClient

client = MongoClient(
  "mongodb+srv://admin:Hlw7V8CtNJ0hXsgk@cluster0.jrxen8d.mongodb.net/?retryWrites=true&w=majority"
)

db = client['stock-prices'] # Note: "stock-prices" is the name of the Database 
collection = db.prices      # Note: "prices" is the name of the collectionimport pymongo

# write your queries here (#1)
all_stocks = list(collection.find({}))
print(all_stocks)
