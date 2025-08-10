'''
Nested if-else statement allows you to check multiple conditions by placing one if-else statement inside another.   
create basic if-else statement:

age = 18
title = "None"
if age >= 18:
    title = "Adult"
else:
    title = "Minor"

Now let's add a nested condition inside: 
age = 18
title = "None"
if age >= 18:
    if age >= 65:
        title = "Senior Adult"
    else:
        title = "Adult"
else:
    if age < 13:
        title = "Child"
    else:
        title = "Teenager"
    
another example:

age = 18
title = "None"
allowed_to_drink = False
if age >= 18:
    title = "Adult"
    if age >= 21:
        allowed_to_drink = True
    else:
        allowed_to_drink = False
else:
    title = "Minor"

'''

#Challenge1:
'''
Write a program that determines eligibility for a movie based on age and parental guidance.

Your program should:

Create a variable age and assign it a value from input.
Create a variable with_parent and assign it a True/False value from input.
Create a variable named message with the value of "None".
Use nested if-else to determine what string to put in message: 
If age is 18 or older, set "You can watch any movie".
If age is under 18: 
If with_parent is True, set "You can watch PG-13 movies".
If with_parent is False, set "You can only watch G-rated movies".

'''

'''
age = int(input('age of a person: '))
with_parent = input('does parent present? (True or False): ') == "True"
message = "None"

if age >= 18:
    message = "You can watch any movie"    
else:
    if with_parent == True :
        message = "You can watch PG-13 movies"
    else:
        message = "You can only watch G-rated movies"

print(f'message is, {message}')

'''



#Challenge 2:
'''
Create a program for a game character creation system. The requirements are:

The character's level determines what weapons they can use:

Level 1-5: Can only use Basic weapons
Level 6-10: Can use Advanced weapons if they completed training
Level 11+: Can use any weapon

Set level_message variable with these messages based on the conditions:

If level 1-5: Basic weapons only
If level 6-10 and no training: Need weapon training first
If level 6-10 and has training: Access to advanced weapons granted
If level 11+: Access to all weapons granted
If level is 0 or negative: Invalid level

'''

level = int(input('Enter the level: '))
has_training = input('Do you have training? (Yes or No): ') == 'Yes'
level_message = "None"

if level >=1 and level <=5:
    level_message = "Basic weapons only"
elif 6 <= level <= 10:
    if has_training == True:
        level_message = 'Access to advanced weapons granted'
    else:
        level_message = 'Need weapon training first'
elif level >= 11:
    level_message = "Access to all weapons granted"
else:
    level_message = 'Invalid level'

print(f'level_message={level_message}')


