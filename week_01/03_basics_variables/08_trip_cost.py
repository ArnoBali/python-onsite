'''
Receive the following arguments from the user:
    - miles to drive
    - MPG of the car
    - Price per gallon of fuel

Display the cost of the trip in the console.

'''

miles = int(input("please input miles to drive:" ))
mpg  = int(input("please input MPG of the car:" ))
p_gallon = int(input("please input Price per gallon of fuel:" ))

cost_trip =  (miles / mpg) * p_gallon

print(cost_trip)