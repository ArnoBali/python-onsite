'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''

with open('words.txt','r') as fin:
   words = fin.readlines()

print(words)

longest = 0
smallest = 100

for word in words:
    if len(word) > longest:
        longest = len(word)

    if len(word) < smallest:
        smallest = len(word)

for word in words:
    if len(word) == longest:
        print(word)
    if len(word) == smallest:
        print(word)

print(len(words))
