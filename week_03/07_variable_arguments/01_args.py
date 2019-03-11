'''
Write a script with a function that demonstrates the use of *args.

'''

def func(name, *args):
    return f"{name}, {args}"


print(func('Arno'))

print(func('Arno', 'Peter', 'Robert'))