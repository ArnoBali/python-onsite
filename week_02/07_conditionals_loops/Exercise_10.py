'''
Write a script that prints out all the squares of numbers
from a user inputed lower to a user inputed upper bound.

Use a for loop that demonstrates the use of the range function.

'''

input1 = 1 + int(input("Upper bound: "))
input2 = int(input("Lower bound: "))

for i in range(input2, input1):
    print(i**2)

