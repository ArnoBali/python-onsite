'''
http://docs.nomics.com/
Using the nomics API, repeatedly fetch the price of Bitcoin for a duration of 10 minutes.
Store each value in a dictionary that uses the time of query as a key.

After the script stopped running, determine programmatically at what query time the price
was the highest, and when the lowest.

HINTS:
- request an API key first and remember to include it in your queries
- the /prices endpoint of the nomics API can be used for achieving this task
- remember to use packages from the standard library, e.g. for time keeping and dates

BONUS: Explore the logging package for easier tracking

'''
from secrets import tokens
import requests
import time

start_time = time.time()
print(f"Start time: {start_time}")
t_end = start_time + 10 * 1


CRYPTO_KEY = tokens['CRYPTO_API']


url = f'https://api.nomics.com/v1/prices?key={CRYPTO_KEY}'
prices = requests.get(url)

bitcoin_price = prices.json()[105]['price']

btc_dict = {}

while time.time() < t_end:
    btc_dict[time.time()] = bitcoin_price
    continue

max_value = max(btc_dict.values())
for CRYPT0_KEY, value in btc_dict.items():
    if value == max_value:
        print(f"At {CRYPTO_KEY} the highest BTC price at {value} occurred! ")

