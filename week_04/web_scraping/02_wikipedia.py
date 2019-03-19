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
session = requests_html.HTMLSession() #creation of instance of module's Class?
html = requests_html.HTML
ses = session.get(url)

# wiki1 = ses.html.find('#mw-content-text > div > table.infobox.geography.vcard > tbody', first=True)
# print(wiki1.html)
# print(wiki1.html)

wiki2 = ses.html.find('img')
wiki2b = list(ses.html.absolute_links)

#mw-content-text > div > table.infobox.geography.vcard > tbody > tr:nth-child(4) > td > a > img
# print(wiki2[0].attrs['src'])
# print(wiki2[1].attrs['src'])

# match = ses.html.find('img')
# print(match.text)

# print(wiki2b[0])
# print(wiki2b[1])



# print(titles)

wiki3 = ses.html.xpath('//*[@id="mw-content-text"]/div/p[2]/text()[1]')
print(wiki3[0])


titles = ses.html.find('mw-headline')

wiki4_title = ses.html.xpath('//*[@class="mw-headline"]')
wiki4_links = list(ses.html.absolute_links)

for i in range(0,len(wiki4_title)):
    title = wiki4_title[i].attrs['id']
    with open('titles_links.txt', 'a') as fout:
        fout.write(f"{title} \n")

for i in range(0,len(wiki4_links)):
    link = wiki4_links[i]
    with open('titles_links.txt', 'a') as fout:
        fout.write(f"{link} \n")


print(wiki4_title[0].attrs['id'])
# print(wiki4_links[0])
