'''

Building on the dog class from the previous example, create a subclass of the dog class
with at least one additional attribute. Also, override the sleep() and eat() methods to act
slightly different.

Create and object of this class and demonstrate it's functionality.

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

class Dog_tail(Dog):
    def __init__(self, name, color, age, tail):
        super().__init__(name, color, age)
        self.tail = tail

    def eat(self, food_item, amount):
        self.is_hungry = False
        self.percent_full += 30
        return f"The dog ate {amount} of {food_item}"

    def dog_sleep(self):
        self.is_hungry = True
        self.percent_full -= 80
        return time.sleep(1)

japie = Dog_tail("japie", "orange", 12, 'Yes')
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