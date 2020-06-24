# Stock Price Queries in MongoDB

### The Goal

We've got a database with historical stock prices from Amazon (AMZN), Apple (AAPL), IBM (IBM) and Microsoft (MSFT). The data is stored in a MongoDB where each entry/document is in the following format:

```json
{
	"symbol" : "AMZN",
	"month" : "Mar",
	"year" : 2004,
	"price" : 43.28
}

```

Your challenge will be to query the MongoDB to produce a single result or multiple results according to the descriptions below.

## Environment Setup

We're going to continue working in your Cloud Shell environment, so clone this repository into your environment as you've done before.

You may need to install PyMongo and dnspython in the Cloud Shell IDE to help connect to the MongoDB database:

```bash
sudo pip3 install pymongo
sudo pip3 install dnspython
```

You can also echo these installations to the startup script if you want to install them permanently - ask an Upperline Code team member for support on this if you want to do it. 

Be aware that you'll need to start by specifying the name of the database you want to connect to. This database for this lab is called `'stock-prices'`. 

### Running stocks.py

To run the `stocks.py` file, type `python3 stocks.py` in the Terminal in your IDE. Anything you `print()` will be shown in the Terminal, too. Bear in mind that while our intro to MongoDB included being able to SEE the entries on the MongoDB dashboard GUI (graphical user interface), this lab will be done entirely with queries, so you'll ONLY be able to see the content you print to the terminal. 

# Challenges

## Warmups

#### 1. List all entries in the `prices` collection in the `stock-prices` database.

> You'll notice we've given you a bit help on this one to start out.
> 
> Any query that may return multiple documents is returned as a `Cursor`, and this is a data structure we haven't seen before. To convert the `Cursor` into something you're more familiar with, we can wrap the result in the `list()` method, in a similar way to how we used `dict()` before:
>
> ```python
> data = list(collection.find({...}))
> ```
>
> You can also iterate over the `Cursor` using a `for` loop:
>
> ```python
> for entry in data:
> 	print(entry)
> ```
> 
> So we've given you the search query solution. What's missing?

#### 2. List all historical Microsoft stock prices

#### 3. List all historical stock prices from 2004

#### 4. List all historical stock prices from September

#### 5. List all historical stock prices from September 2004

#### 6. List all historical stock prices in order from lowest value to highest value

#### 7. List all historical stock prices in order from highest value to lowest value

#### 8. List the first 5 historical stocks in the database.

#### 9. Find an historical stock that was valued at $100.52.

#### 10. How many entries are there in the database for Apple stock prices?

> You can, of course use standard `len()` functionality to count items in a list, but if you want to try something a bit more MongoDB specific, here's a bit of help:
>
> - [MongoDB .count() Method](https://docs.mongodb.com/manual/reference/method/db.collection.count/) - It's worth knowing that MongoDB documentation is written in JavaScript, and we're writing in Python, so you can also cross-reference these with the [PyMongo Documentation](https://pymongo.readthedocs.io/en/stable/api/pymongo/cursor.html#pymongo.cursor.Cursor.count) for the same .count() method. 
>
> While balancing TWO different pieces of documentation is difficult, we've found that the official documentation (written in JavaScript) is a lot easier to understand, so we usually recommend reading there first to see WHAT you want to do, and then checking the PyMongo documentation (written in Python) to make sure that the syntax is the same (it often is), or adjust the syntax a little if it happens to be different. 

## Showtime

#### 11. List the first 10 Apple entries in the database.

#### 12. List the January IBM stock prices from lowest to highest.

#### 13. List all historical stock prices over $200.00

> Here's a bit of help:
> 
> - [MongoDB Query Comparison Operators](https://docs.mongodb.com/manual/reference/operator/query-comparison/)
>
> This is a situation where the official (JavaScript) documentation doesn't work exactly the same in Python, but the fix is actually super easy. While JavaScript objects can take symbols like `$gt` as keys in key-value pairs, Python is going to need a string version of those same terms, for example `"$gt"` instead of just `$gt`. 
> 
> This is an example of a situation where the PyMongo documentation doesn't even *have* a comparable page, because they expect you to look at the JavaScript documentation and infer that it's probably the same. They do, however, include an [example of how to use one operator](https://pymongo.readthedocs.io/en/stable/tutorial.html?highlight=query#range-queries) in the tutorial, so if you're feeling stuck, looking at the JavaScript example, and want to see a Python example, that's a good place to start. 

#### 14. List all historical stock prices less than $10.00.

#### 15. What company's (or companies') stock was valued at $9.78 in October, 2000? Return only the name of the company.

#### 16. What was the price of Amazon's Stock in August, 2006? Return only the price.

#### 17. What was the highest historical price of Microsoft's stock? Return only the price.

#### 18. For how many months (in the historical database) has Apple's stock price been greater than $100.00? Return only the number of months.

## Additional Documentation

- [MongoDB Query Operators](https://docs.mongodb.com/manual/reference/operator/query/)
