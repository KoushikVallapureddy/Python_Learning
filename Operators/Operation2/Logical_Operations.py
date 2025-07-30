"""
Logical operations are used to combine conditional statements in Python.
Python has three logical operators: `and`, `or`, `not`.
"""
"""
Lets see how 'and' operator works
The 'and' operator returns True if both statements are true.
example: 
    a=true or 1
    b=true or 1
    result = a and b
    result will be True or 1
The 'and' operator returns False if any one of the statements is false.
    a=true or 1
    b=false or 0
    result = a and b
    result will be False or 0

Lets see how 'or' operator works
The 'or' operator returns True if at least one of the statements is true.
example:
    a=true or 1
    b=false or 0
    result = a or b
    result will be True or 1
The 'or' operator returns False if both statements are false.
    a=false or 0
    b=false or 0
    result = a or b
    result will be False or 0   

Lets see how 'not' operator works
The 'not' operator reverses the result of the boolean expression.
example:
    a=true or 1
    result = not a
    result will be False or 0
The 'not' operator returns True if the statement is false.
    a=false or 0
    result = not a
    result will be True or 1


Truth table for 'and' operator:
| A     | B     | A and B |
|-------|-------|---------|
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |         

Truth table for 'or' operator:
| A     | B     | A or B  |
|-------|-------|---------|
| True  | True  | True    |
| True  | False | True    |
| False | True  | True    |
| False | False | False   |

Truth table for 'not' operator:
| A     | not A  |
|-------|--------|
| True  | False  |
| False | True   |


"""

#Code
'''Complete the code to determine if a person is eligible to vote based on their age and citizenship status.
A person is eligible to vote if they are at least 18 years old and a citizen.'''

age = 20
is_citizen = 0
# Check if the person is eligible to vote
is_eligible_to_vote = age >= 18 and is_citizen
# Print the result
print("Is the person eligible to vote?", is_eligible_to_vote)


#Challenge

a1 = 1
a2 = False
a3 = a1 and a2
print(f'the result of a3 is {a3}')  # Expected output: False
print('The result of a3 is', a3)

#Challenge 2
num1 = 50
num2 = 20
num3 = (num1 * num2) > (num1 + num2*2)
print(f'The result of num3 is',num3) 


#Challenge 3
"""
Replace the values of variables a, b, and c with boolean values (True or False) so that result evaluates to True.
result will be True when the expression (a or b) and not c is true. Use the logical operators or, and, and not to solve this challenge.
"""

a= True
b= False
c= False
result = (a or b) and not c
print('the result is', result)


#Challenge 4
"""
Replace the values of variables a, b, and c with boolean values (True or False) so that result evaluates to True.
"""
a = True
b = True
c = False
d = a and b and (not c)
print(f"d = {d}")
