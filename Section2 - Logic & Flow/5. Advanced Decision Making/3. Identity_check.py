'''
In Python, the is and is not operators are used to check the identity of objects. Unlike the == operator, which checks if two variables have the same value, the is operator checks if two variables refer to the exact same object in memory.

Basic usage of is:
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]
    print(a is b)  # Output: True
    print(a is c)  # Output: False

In this example, a and b refer to the same list object, so a is b returns True. However, a and c are different list objects with the same values, so a is c returns False.

Basic Usage of is not:
    x = 5
    y = 5
    z = 10
    print(x is not y)  # Output: False
    print(x is not z)  # Output: True

Here, x and y refer to the same integer object (due to Python's optimizations for small integers), so x is not y returns False. 
x and z are different objects, so x is not z returns True.

Identity checks are particularly useful when you want to determine if two variables are pointing to the same object in memory, rather than just
having the same value.
'''

#Challenge1:

'''
Create two variables, list1 and list2, where:
    list1 refers to a list [1, 2, 3].
    list2 is assigned to the same object.
Use the is operator to check if list1 and list2 refer to the same object.
Use the is not operator to check if list1 and list2 refer to different objects.
Print the results of the checks.
'''
list1 = [1, 2, 3]
list2 = list1
print(list1 is list2)
print(list1 is not list2)



#Challenge2:
'''
Create a function named compare_strings that takes two strings, str1 and str2, as arguments. The function should perform the following operations:
    Check if str1 is a substring of str2.
    Check if str2 starts with str1.
    Check if str2 ends with str1.
    Check if str1 and str2 are equal (case-insensitive).
    Return a dictionary containing the results of these operations, with the keys "is_substring", "starts_with", "ends_with", and "is_equal".
'''

def compare_strings(str1, str2):
    result = {
        "is_substring": str1 in str2,
        "starts_with": str2.startswith(str1),
        "ends_with": str2.endswith(str1),
        "is_equal": str1.lower() == str2.lower()
    }
    print(result)
    
    

str1 = input()
str2 = input()
compare_strings(str1, str2)