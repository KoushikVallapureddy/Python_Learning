'''
Comparison Operations:
Compaparison operations are used to compare between two operands.
Sometimes we need to check whether an operand is greater than, less than, equal to, or not equal to another operand. 
The following operations are used for comparions:
    1. == Equal to. Example: 1 == 2 returns False
    2. != Not equal to. Example: 1 != 2 returns True
    3. > Greater than. Example: 1 > 2 returns False
    4. < Less than. Example: 1 < 2 returns True
    5. >= Greater than or equal to. Example: 1 >= 2 returns False
    6. <= Less than or equal to. Example: 1 <= 2 returns True
The comparison operations returns boolean values (True or False) based on the comparison of the operands.
For example:
var1 = 10
var2 = 20
var3 = var1 == var2
print(var3)  # Output: False
'''
#Code:
"""
Write a script that initializes 2 variables a1 and a2 with the values 9.9 and 9.11 (accordingly).
After that initialize another variable a3 that will hold whether a1 is bigger than a2.
"""

a1 = 9.9
a2 = 9.11
a3 = a1 > a2
a4 = a1 == a2
a5= a1 != a2
a6 = a1 < a2
print(f'a1={a1}, a2={a2}, a3={a3}, \na4={a4}, a5 = {a5}, a6 = {a6}') 



