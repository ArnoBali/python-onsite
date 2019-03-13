'''
Demonstrate how to create a generator object. Print the object to the console to see what you get.
Then iterate over the generator object and print out each item.

'''


my_list = [1, 2, 3, 5, 42]

new_li = [x+1 for x in my_list]
print(new_li)

gen = (x+1 for x in my_list)
print(gen)

for x in gen:
    print(x)

