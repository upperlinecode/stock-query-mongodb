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

## Running stocks.py

To run the `stocks.py` file, run `python stocks.py` in the Terminal in CS50. Anything you `print()` will be shown in the Terminal, too.

# Challenges

### List all entries in the `prices` collection in the `stock-prices` database.

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

### List all historical Amazon stock prices

### List all historical Microsoft stock prices

### List all historical stock prices from 2004

### List all historical stock prices from September

### List all historical stock prices from September 2004

### List all historical stock prices in order from lowest value to highest value

### List all historical stock prices in order from highest value to lowest value

### List all historical stock prices in order from lowest value to highest value


> https://docs.mongodb.com/manual/reference/operator/query/

> https://docs.mongodb.com/manual/reference/operator/query-comparison/