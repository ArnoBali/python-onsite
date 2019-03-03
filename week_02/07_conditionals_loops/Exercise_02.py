'''
Take in a number from the user and print "Monday", "Tuesday", ...
"Sunday", or "Other" if the number from the user is 1, 2,... 7,
or other respectively. Use a "nested-if" statement.

'''

input_ = int(input("Please input a number between 1 - 7: "))

if input_ > 1:
    if input_ > 2:
        if input_ > 3:
            if input_ > 4:
                if input_ > 5:
                    if input_ > 6:
                        print('Sunday')
                    else:
                        print('Saturday')
                else:
                    print('Friday')
            else:
                print('Thursday')
        else:
            print('Wednesday')
    else:
        print('Tuesday')
else:
    print('Monday')



# if input_ == 1:
#     print('Monday')
# elif input_ == 2:
#     print('Tuesday')
# elif input_ == 3:
#     print('Wednesday')
# elif input_ == 4:
#     print('Thursday')
# elif input_ == 5:
#     print('Friday')
# elif input_ == 6:
#     print('Saturday')
# elif input_ == 7:
#     print('Sunday')
# else:
#     print('Dude, between 1-7!')