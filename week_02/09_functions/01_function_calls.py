'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''


def car():
    return "Sweet car man!"

def new_car(wheels, color):
    return f"My new car has {wheels} wheels, and is {}."

def old_car(year):
    if year < 2000:
        return "that's an really old car"
    elif year < 2015:
        return "that's an old car"
    else:
        return "that's a new car man!"