'''
Building on the dog exercise in the previous section:

1. Create a dog class and make the functions from the last class methods of the dog class.

2. Add an __init__() method that sets the following attributes:

    - name
    - color
    - age
    - is_hungry (should be a boolean)
    - percent_full

    Note: is_hungry should default to False, and percent_full should default to 100.

3. Change the sleep() method so that when the method is called, the attribute is_hungry is set to True
    and the attribute percent_full is decremented by 20 percent.

4. Change the eat() method so that when the method is called, the attribute is_hungry is set to False
    and the attribute percent full is incremented to 100.

5. Add a __str__() method to print out all the information about the dog.

6. Create at least two objects of the dog class to demonstrate the functionality.

'''

import time

class Dog:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
        self.is_hungry = False
        self.percent_full = 100

    def bark(self):
        return "'bark bark!'"

    def eat(self, food_item, amount):
        self.is_hungry = False
        self.percent_full = 100
        return f"The dog ate {amount} of {food_item}"

    def dog_sleep(self):
        self.is_hungry = True
        self.percent_full -= 50
        return time.sleep(1)

    def __str__(self):
        return f"This dog is named '{self.name}', has color '{self.color}' and is '{self.age}' years old!"

japie = Dog("japie", "orange", 12)
sjaak = Dog("Sjaak", "transparent", 4)

print(japie)
print(sjaak)

while True:
    if japie.percent_full > 0:
        print(japie.bark())
        zzz = input("Should the dog go to sleep? ")
        print(zzz)

        if zzz == "Yes":
            print("zzz zzz zzz zzz zzz zzz zzz zzz")
            japie.dog_sleep()

            feed = input("Do you want to feed the dog? ")

            if feed == "Yes":
                food_item = input("What do you want to feed the dog? ")
                food_amount = input("In what amount? ")
                print(japie.eat(food_item, food_amount))

                # print("zzzzzz")
                # japie.dog_sleep()

                print("happy doggie!")
                break
            else:
                japie.bark()
        else:
            japie.bark()
    else:
        print(f'{japie.name} is sleeping with the fishes..!')
        break