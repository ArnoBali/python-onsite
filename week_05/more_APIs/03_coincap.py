'''
Sign up for an API key with the new coinmarketcap API.

Using their documentation, fetch all listed cryptocurrencies.
From the result, create a new JSON file that includes the following:
* cmc_rank
* name
* symbol
* platform
* quote

Save that info to a file.

'''
import requests
import pprint
import json
from secrets import COIN_MARKET_KEY

cmk = COIN_MARKET_KEY

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' #?sort=market_cap&start=0&limit=10&cryptocurrency_type=tokens&convert=USD,BTC


headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': cmk
        }
session = requests.Session()
session.headers.update(headers)

response = session.get(url)
data = json.loads(response.text)
cryptos = data['data']

crypto_list = []

for c in cryptos:
    crypto_dict = {}

    crypto_dict['cmc_rank'] = c['cmc_rank']
    crypto_dict['name'] = c['name']
    crypto_dict['symbol'] = c['symbol']
    crypto_dict['platform'] = c['platform']
    crypto_dict['quote'] = c['quote']

    crypto_list.append(crypto_dict)

with open('crypto.json', 'w') as outfile:
    json.dump(crypto_list, outfile, sort_keys=True, indent=4, separators=(',', ':'))