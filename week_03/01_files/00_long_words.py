'''
Write a program that reads in the file words.txt and prints only the
words with more than 20 characters (not counting whitespace).

Source: http://greenteapress.com/thinkpython2/html/thinkpython2010.html

'''

with open('words.txt','r') as fin:
   words = fin.readlines()

print(words)

for word in words:
    if len(word) > 20:
        print(word)