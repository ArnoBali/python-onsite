'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

with open('words.txt', 'r') as fin:
    words = fin.readlines()
    # word_reverse = words.reverse()

# print(type(words))
# words_reverse = reversed(words)
# print(words_reverse)

with open('words_reverse.txt', 'a') as fout:
    for i in words:
        words_reverse = fout.write(i[::-1])

