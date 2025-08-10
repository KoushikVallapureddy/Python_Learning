'''Modulo operator:
THe module operator tells you what is left over after dividing one number by another.
in simple terms, it is the remainder of a division operation.
result = dividend % divisor
    dividend: the number to be divided
    divisor: the number by which to divide
    result: the remainder after division
for example:
    10 % 3 = 1  # because 10 divided by 3 is 3 with a remainder of 1. So the result is 1
    20 % 4 = 0  # because 20 divided by 4 is 5 with no remainder. So the result is 0
    15 % 6 = 3  # because 15 divided by 6 is 2 with a remainder of 3. So the result is 3

Use the / operator for regular division. For example: 7 / 2 equals 3.5
Use the // operator for integer division. For example: 7 // 2 equals 3 (not 3.5)

Ususally modulo is used to check if a number is even or odd.
    if a number is even, dividing it by 2 will result in 0 remainder.
    if a number is odd, dividing it by 2 will result in 1 remainder.

'''

#Modulo operator

a = 10
b = 3
c = 15
d = a % 3
e = b % 2
f = c % 6
print(f'a ={a}, b={b}, c={c}, d={d}, e={e}, f={f}')
print(f"a={a}")
print(f"b={b}")
print(f"c={c}")
print(f"d={d}")
print(f'e={e}')
print(f'f={f}')


#Challenge:
"""
Write a program that initializes 4 variables a, x, y, z with the values 10, 5, 3, and 2. 
after initialization, calculate the following:
    b hold the result of integer division of a by x. in another code a holds the reminder of a divided by x
    c holds the results of integer of x divided by y. in another code x holds the reminder of x divided by y
    d holds the result of integer of y divided by z. in another code y holds the reminder of y divided by z
    e hold the result of integer of z divided by a. in another code z holds the reminder of z divided by a
"""

#code1:
a=10
x=5
y=3
z=2
b=a // x
c=x // y
d=y // z
e=z // a
print(f'a={a}, x={x}, y={y}, z={z}, b={b}, c={c}, d={d}, e={e}')

# code2:
a=10
x=5
y=3
z=2
b=a%x
c=x%y
d=y%z
e=z%a
print(f'a={a}, x={x}, y={y}, z={z}, b={b}, c={c}, d={d}, e={e}')