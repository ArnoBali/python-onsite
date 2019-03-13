'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''

nums = range(1, 1000000)

gen = (num for num in nums if num % 1111 == 0)

for x in gen:
    print(x // 1111)
