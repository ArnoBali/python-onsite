'''
Using python's request library, retrieve the HTML of the website you created
that now lives online at <your-gh-username>.github.io/<your-repo-name>

BONUS: extend your python program so that it reads your original HTML file
       and returns True if the HTML from the response is the same as the
       the contents of the original HTML file.
'''

# from requests_html import HTMLSession

import requests_html

url = "https://arnobali.github.io/food_menus_Outpost_Ubud/"
session = requests_html.HTMLSession()
r = session.get(url)
# r.html.render()

# for link in r.html.absolute_links:
#     print(link)

a = r.html.html

with open('outpost_food.html', 'r', encoding='utf-8') as fin:
    if fin.read() == a:
        print(True)

# print(a)

