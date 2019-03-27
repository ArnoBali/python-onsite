'''
Write a lambda function that takes in 3 numbers and returns the sum of the numbers.

'''

my_list = [3, 5, 42]
#
# y = 0

sum = lambda : 1 + 4 + 5
print(sum())

sum2 = lambda a,b,c: a + b + c

print(sum2(my_list[0],my_list[1],my_list[2]))