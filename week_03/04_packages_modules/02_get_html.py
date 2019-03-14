'''
In 3 lines of code, fetch the HTML text from codingnomads' main page
and print it to your console.

TIP:
- if you wonder what to use, google something like
    "most popular python package"
- if you run into encoding/decoding errors, you're experiencing something
    very common. head over to SO and find a solution!

'''
import requests

url = "https://codingnomads.co/"

res = requests.get(url)


with open('codingnomads.html', 'w', encoding='utf-8') as fout:
    fout.write(res.text)
