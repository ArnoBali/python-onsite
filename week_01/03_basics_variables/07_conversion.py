'''
Celsius to Fahrenheit:

Write the necessary code to read a degree in Celsius from the console
then convert it to fahrenheit and print it to the console.

    F = C * 1.8 + 32

Output should read like - "27.4 degrees celsius = 81.32 degrees fahrenheit"

NOTE: if you get an error, look up what input() returns!

'''

c = int(input("please input degrees celsius:" ))


fahrenheit = ( c * 1.8 ) + 32
print(fahrenheit)

print(f"{c} degrees celsius = {fahrenheit} degrees fahrenheit")



''' 
fahrenheit = int(input("Please enter: degrees fahrenheit "))

celcius = (fahrenheit - 32) * (5 / 9)

print(str(fahrenheit) + " degrees fahrenheit = " + str(celcius) + " degrees celcius" )
'''