'''
Use the countries API https://restcountries.eu/ to fetch information
on your home country and the country you're currently in.

In your python program, parse and compare the data of the two responses:
* Which country has the larger population?
* How much does the are of the two countries differ?
* Print the native name of both countries, as well as their capitals

'''

import requests

url_country1 = 'https://restcountries.eu/rest/v2/name/netherlands?fullText=true'
url_country2 = 'https://restcountries.eu/rest/v2/name/belgium?fullText=true'
h = requests.get(url_country1)
c = requests.get(url_country2)
country1 = h.json()
country2 = c.json()

print(country1[0]['population'])
print(country2[0]['population'])

if (country1[0]['population']) >= (country2[0]['population']):
    print("NL rules!")
else:
    print("booeeh Belgium")

diff_pop = (country1[0]['population']) - (country2[0]['population'])
print(diff_pop)

print(f"{country1[0]['name']}: {country1[0]['capital']}")
print(f"{country2[0]['name']}: {country2[0]['capital']}")

