'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple


Notes:

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

'''

list_ = []
r = 6
for i in range(r):
    input_ = int(input("Please enter a number for the list: "))
    list_.append(input_)

list_.sort()

print(list_)

tuple_list = []

for i in range(0, r, 2):
    tuple_list.append((list_[i], list_[i+1]))

print(tuple_list)
