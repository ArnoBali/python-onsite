'''
Print out every prime number between 1 and 100.

'''

# prime numbers can only be divided by 1 and themselves

for x in range(2, 100):
    flag = True
    for y in range(2, x):

        if x % y == 0:
            flag = False
            break

    if flag == True:
        print(x)

