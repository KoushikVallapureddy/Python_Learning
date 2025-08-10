'''
Recap- Product list:

Challenge1:
Write a function named prod which gets a list of numbers as argument and returns the product of all the numbers in the list.
Reminder, product is the multiplication of all the numbers, for [1, 2, 3], return 6 = 1 * 2 * 3.


def prod(lst):
    result = 1
    for num in lst:
        result *= num
    return result

'''

#Challenge2:
'''
Write a function named reverse which gets a list of numbers as argument and returns the reversed list.
For example, for [1, 2, 3], the expected output is [3, 2, 1].
Don't use the reverse list builtin function!
'''

def reverse(lst):
    reversed_list = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list