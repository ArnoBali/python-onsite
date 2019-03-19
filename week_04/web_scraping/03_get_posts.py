'''
Create an account at freecycle or use the following:
user: martin-martin
pwd:  bali2019

Using python's request_html library:
* log in to the website
* navigate to the site that contains all posts for the Denver, CO group
* retrieve all post titles from the first page
* save the titles to a file called 'denver_posts.txt'

BONUS: use pagination features to retrieve all posts of all pages in the group
       and save them to the file

'''

import requests_html

url_home = 'https://my.freecycle.org/login'
url_denver = 'https://groups.freecycle.org/group/DenverCO/posts/all'
payload = {'username':'martin-martin', 'pass': 'bali2019'}
session = requests_html.HTMLSession()

ses_get = session.get(url_home)
ses_post = session.post(url_home, data=payload)
links = ses_post.html.absolute_links

for link in links:
    if link.endswith("DenverCO"):
        url = link

print(url)

ses_get2 = session.get(url)
# print(ses_get2.html.find("#group_posts_table")[0])

class1 = ses_get2.html.find(".candy1")
class2 = ses_get2.html.find(".candy2")
class_all = class1 + class2

# for i in class_all:
#     print(i.html.a.text)

with open('denver_posts.txt', 'a') as fout:
    for i in class_all:
        for y in range(3):
            img = i.xpath('//a')[y]
            fout.write(f"{img.text}\n")


