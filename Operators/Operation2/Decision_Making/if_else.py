'''
if allows us to execute particular code if a condition is met, but when if we want to execute something else if the condition is not met?
for that we have else statement:
example: 
age = 15
status = "None"
if age >= 18:
    status = "Adult"
else
    status = "Young"

In above example, age is smaller than 18 which means it enter the else code and status will hold "Young". 
We can even make it more profound using the elif statement.

age = 30
status = "None"
if age < 18:
    status = "Young"
elif age >= 18 and age  <= 65:
    Status = "Adult"
else:
    Status = "Old"

We can add as many elif statements as we want:
if condition1:
    code
elif condition2:
    code
elif condition3:
    code

'''
#Challenge1:
"""
You are given a code which gets as input a number that indicates the wind speed and stores it in a variable named wind.

Your task is to initialize variable status based on the conditions:

"Calm" if wind is smaller than 8,
"Breeze" if wind is between 8 and 31 (including 8 and 31).
"Gale" if wind is between 32 and 63 (including 32 and 63)
"Storm" otherwise

"""
'''
wind = int(input('Speed of the wind is: '))
status = 'unset'
if wind < 8:
    status = "Calm"
elif 8 <= wind <= 31:
    status = "Breeze"
elif 32 <= wind <= 63:
    status = "Gale"
else:
    status = "Storm"

print(f'status of the wind = {status}')


'''

#Challenge 2:
'''
You are given a code which gets as input a number that indicates the temperature in Celsius and stores it in a variable named temperature.

Your task is to initialize variable weather based on the following conditions:

"Freezing" if temperature is below 0,
"Cold" if temperature is between 0 and 15 (including 0 and 15).
"Mild" if temperature is between 16 and 25 (including 16 and 25)
"Hot" otherwise

'''
'''
temperature = int(input('Temperature in Celsius: '))
status = "None"

if temperature < 0 :
    status = "Freezing"
elif temperature >= 0 and temperature <= 15 : 
    status = 'Cold'
elif 16 <= temperature <= 25:
    status = "Mild"
else:
    status = 'Hot'

print(f'Weather outside is: {status}')

'''


