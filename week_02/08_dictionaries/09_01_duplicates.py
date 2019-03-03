'''
Using a dictionary, write a function called has_duplicates that takes
a list and returns True if there is any element that appears more than
once.


'''

list_ = [1, 4, 2, 6, 4, 3]
# list_ = [1, 4, 2, 6, 3]


l_unique = list(set(list_))

if len(l_unique) < len(list_):
    print(True)
else:
    print(False)
