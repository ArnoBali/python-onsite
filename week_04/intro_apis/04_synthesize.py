'''
Using the Chuck Norris API in combination with the datamuse API
( https://api.chucknorris.io/ - https://www.datamuse.com/api/ )

* Query the chucknorris api for a sentence
* Use the last word of that sentence to send a query to the Datamuse API
  and use the rel_rhy (or rel_nry) query parameter to fetch a word that rhymes
* Repeat a coupe of times and store the sentences and rhyme words
* Synthesize the collected results into an avant-garde poem and present it to class ;)

'''

import requests

url_chuch = 'https://api.chucknorris.io/jokes/random'
chuck = requests.get(url_chuch)

chuck_sentence = chuck.json()['value']

word_list = chuck_sentence.split()

rym_word = word_list[-1].rstrip('!.')
url_muse = f'https://api.datamuse.com/words?rel_rhy={rym_word}'

muse = requests.get(url_muse)

print(muse.json()[0]['word'])
print(chuck_sentence)

with open('chuch_rym', 'a') as fout:
    fout.write(f"{chuck_sentence}\n {muse.json()[0]['word']} \n")