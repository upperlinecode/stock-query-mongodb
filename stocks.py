import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb+srv://student:PqyqrY2aEC22B5SB@cluster0-ya1yr.mongodb.net/stock-prices?retryWrites=true")
db = client['<database>'] #Make sure to replace this with the name of the database!
collection = db.prices

# write your queries here
stocks = list(collection.find({}))
print(stocks)

