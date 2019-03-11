'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''

my_list = [1, 4, 5, 3, 754, 543]

def my_enumerate(iterable):
    for key, value in enumerate(iterable):
        print(key, value)

print(my_enumerate(my_list))