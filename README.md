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

We're going to continue working in [ide.cs50.io](https://ide.cs50.io), so clone this repository into CS50 as you've done before.

### Running stocks.py

To run the `stocks.py` file, type `python stocks.py` in the Terminal in CS50. Anything you `print()` will be shown in the Terminal, too.

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

#### 2. List all historical Microsoft stock prices

#### 3. List all historical stock prices from 2004

#### 4. List all historical stock prices from September

#### 5. List all historical stock prices from September 2004

#### 6. List all historical stock prices in order from lowest value to highest value

#### 7. List all historical stock prices in order from highest value to lowest value

#### 8. List all historical stock prices in order from lowest value to highest value

#### 9. List the first 5 historical stocks in the database.

#### 10. Find an historical stock that was valued at $100.52. 

## Showtime

#### 11. List the first 10 Apple entries in the database.

#### 12. List the January IBM stock prices from lowest to highest.

#### 13. List all historical stock prices over $200.00

> Here's a bit of help:
> 
> - [MongoDB Query Comparison Operators](https://docs.mongodb.com/manual/reference/operator/query-comparison/)




## Additional Documentation

- [MongoDB Query Operators](https://docs.mongodb.com/manual/reference/operator/query/)