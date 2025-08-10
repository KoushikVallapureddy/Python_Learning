'''
As of now we stored values that we thought about in variables. Programs usually don't work this way. We receive values from an outer source, a user for example.
To get input from a user or the system we need to write:
var = input()
This will store input in the variable var.
    The input is always of type string. For example, if the input is 56 then var will hold the string "56".
'''
#Challenge:
'''
Write a program that get input from the user (their name), and then outputs Hello, followed by a space and the user's inputted name.

For example, if the user inputs Bob, the expected output is Hello, Bob.

You will need to:

Use input() to get input from the user.
Store the input in a variable.
Print Hello, and the stored variable in the end (add a space after the comma).

'''

'''
user = input()
print('Hello, ',user)
'''

#Challenge 2:

'''Create a program that receives that user's name and age, then calculates and prints how old they will be in 10 years.

The output should be in the format: "In 10 years, [name] will be [age] years old."

You will need to:

Use input() to get the user's name and age.
Store the inputs in variables.
Convert the age to an integer and add 10 to it.
Print the result using an f-string.

'''

'''
name = input('name of the user is? ')
age = int(input('enter the age:' ))

age += 10

print(f'In 10 years, {name} will be {age} years old.')

'''



