'''
Write a script with a function that demonstrates the use of **kwargs.

'''

def func(name, **kwargs):
    return f"{name}, {kwargs}"


print(func('Arno'))

print(func('Arno', '4: Peter', '6: Robert'))