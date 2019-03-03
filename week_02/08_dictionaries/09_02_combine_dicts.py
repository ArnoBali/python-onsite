'''
Create a new dictionary using the three dictionaries below.
Then print out each key-value pair.

'''


dict_1 = {1: 1, 2: 4}
dict_2 = {3: 9, 4: 16}
dict_3 = {5: 25, 6: 36, 7: 49}

l3 = list(dict_1.items()) + list(dict_2.items()) + list(dict_3.items())
dict_4 = dict(l3)

print(l3)
print(dict_4)

for i in dict_4.items():
    print(i)