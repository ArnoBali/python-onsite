'''
Write a script with a function that demonstrates the use of **kwargs.

'''

def fun(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} maps to {value}.")

fun(name="martin", number=1, greeting="hello")
