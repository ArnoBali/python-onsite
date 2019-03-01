'''
Write a program with the following three functions:

    - bark - this function should not take in any arguments and should print the string "bark bark"
    - eat - takes in parameters food_item and amount and prints out "The dog ate <amount> of <food_item>
    - sleep - calls the python sleep method to sleep the program for 5 seconds.



'''
import time

def bark():
    return "'bark bark!'"

def eat(food_item, amount):
    return f"The dog ate {amount} of {food_item}"

def dog_sleep():
    return time.sleep(5)


while True:
    print(bark())
    a = input("Do you want to feed the dog? ")
    print(a)

    if a == "Yes":
        food_item = input("What do you want to feed the dog? ")
        food_amount = input("In what amount? ")
        print(eat(food_item, food_amount))

        print("zzzzzz")
        dog_sleep()

        print("happy doggie!")
        break
    else:
        bark()
