"""Arthimetic shortcuts for Operators:
Python creates a shortcut for self arthimetic operations.
for example, instead of writing:
    a=3
    a = a + 1 # a holds 4
    we can simply write:
    a += 1 # a holds 4
This operation is valid for all arthimetic operations
    for operator + shortcut: +=
    for operator - shortcut: -=
    for operator * shortcut: *=
    for operator / shortcut: /=
    for operator // shortcut: //=
    for operator % shortcut: %=
"""

'''
Task:
Given a code with initialization of value.
Your task is to add the following operationsm in this order:
    Divide value by 4
    Multiply value by 2
    Add 5 to the value
    Subtract 3 from the value
'''

# code"
value = 50
value /= 4
value *= 2
value +=5
value -= 3
print(f'value={value}')  # Expected output: value=27.0
# Explanation:
# 1. Divide 50 by 4: 50 / 4 = 12.5
# 2. Multiply by 2: 12.5 * 2 = 25.0
# 3. Add 5: 25.0 + 5= 30.0
# 4. Subtract 3: 30.0 - 3 = 27.0
# Final result is value = 27.0


""" 
Challenge:
You're given a code with initialization of number.
you're challanged to modify the Number variable using arithmetic shortcuts, in the BODMAS order:
    1. Add 10 to Number
    2. Multiply number by 3
    3. Divide number by 4
    4. Subtract 2 from number.
"""
# code
Number = 20
Number/= 4
Number *= 3
Number += 10
Number -= 2
print(f'Number={Number}')  # Expected output: Number=23.0
# Explanation:
# 1. Divide 20 by 4: 20 / 4 = 5.0
# 2. Multiply by 3: 5.0 * 3 = 15.0
# 3. Add 10: 15.0 + 10 = 25.0
# 4. Subtract 2: 25.0 - 2 = 23.0
# Final result is Number = 23.0


