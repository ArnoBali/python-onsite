'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
	of numbers from the lower bound to the upper bound. Also, calculate the average of numbers.
	Print the results to the console.

	For example, if a user enters 1 and 100, the output should be:
		The sum is: 5050
		The average is: 50.5
'''


input1 = 1 + int(input("Upper bound: "))
input2 = int(input("Lower bound: "))

sum = 0

for i in range(input2, input1):
    sum += i

print(sum)

average = sum / (input1 - input2)

print(average)

