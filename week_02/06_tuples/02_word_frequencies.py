'''
Write a function called most_frequent that takes a string and prints
the letters in decreasing order of frequency.

For example, the follow string should produce the following result.

string_ = 'hello'

Output:
l, h, e, o

For letters that are the same frequency, the order does not matter.

'''

# input_ = input("Please enter a word: ")
input_ = 'hello ubud'

l = list(input_)
# print(l)
l_unique = list(set(input_))
# print(l_unique)

dict_ = {}

for key in l_unique:
    value = l.count(key)
    dict_[key] = value

print(dict_)

l_sort = sorted(dict_, key=dict_.__getitem__, reverse=True)

print(l_sort)

