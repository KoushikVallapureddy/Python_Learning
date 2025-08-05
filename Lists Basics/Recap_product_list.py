'''
Recap- Product list:

Challenge:
Write a function named prod which gets a list of numbers as argument and returns the product of all the numbers in the list.
Reminder, product is the multiplication of all the numbers, for [1, 2, 3], return 6 = 1 * 2 * 3.
'''

def prod(lst):
    result = 1
    for num in lst:
        result *= num
    return result

