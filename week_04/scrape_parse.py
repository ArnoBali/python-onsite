from requests_html import HTMLSession

url = "https://en.wikipedia.org/wiki/Ubud"
session = HTMLSession()
r = session.get(url)
# r.html.render()

for link in r.html.absolute_links:
    print(link)

