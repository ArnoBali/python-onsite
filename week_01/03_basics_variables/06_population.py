'''
In the U.S., if there is:
    - One person who is born every 6 seconds
    - One person who dies every 12 seconds
    - One person who immigrates every 40 seconds

Write the necessary code to display the total population
for the next 3 years (without a leap year).
Let's say the current population is 380,123,456.

'''

y0 = 380123456

born_year = (365*24*60*60)/6
dies_year = (365*24*60*60)/12
immigates_year = (365*24*60*60)/40

y1 = born_year - dies_year + immigates_year

print(y1)
print(y0 + (y1*3))

