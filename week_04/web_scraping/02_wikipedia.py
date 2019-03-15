'''
Using requests_html scrape information from a wikipedia page that interests you.
( you can use: https://en.wikipedia.org/wiki/Ubud )

Collect:
* all the information recorded in the infobox on the right
* 2 links to images on the site
* an interesting fact or quote from the page
* a collection of all the resources (titles and links) related to the page

Store the information in a nicely formatted text file.

'''

import requests_html

url = "https://en.wikipedia.org/wiki/Ubud"
session = requests_html.HTMLSession()
html = requests_html.HTML
ses = session.get(url)

# wiki1 = ses.html.find('#mw-content-text > div > table.infobox.geography.vcard > tbody', first=True)
# print(wiki1.html)
# print(wiki1.html)



wiki2 = ses.html.find('img', first=True).absolute_links
wiki2 = ses.html.absolute_links

print(wiki2)

# match = ses.html.find('img')
# print(match.text)
#
# # x = 0
# # for link in wiki2:
# #     if '.jpg' in link:
# #         x += 1
# #         if x < 3:
# #             print(link)
