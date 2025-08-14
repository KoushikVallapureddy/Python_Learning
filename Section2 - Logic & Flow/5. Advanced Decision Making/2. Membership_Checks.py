'''
Membership Check:

Membership checks in Python let you check if a value exists in a collection like a list, tuple, set, or dictionary using in and not in.

The in operator checks if a value exists:
    fruits = ["apple", "banana", "cherry"]
    print("apple" in fruits)  # True

The not in operator checks if a value does not exist:
    numbers = [1, 2, 3]
    print(4 not in numbers)  # True

For dictionaries, membership checks apply to keys by default:
    my_dict = {"name": "Alice", "age": 25}
    print("name" in my_dict)  # True
    print("Alice" in my_dict)  # False
'''

#Challenge

'''
You are given a list of names and a dictionary of student grades. Write a program that:
    Checks if the name "Alice" is in the list.
    Checks if the name "David" is not in the list.
    Checks if the key "Bob" exists in the dictionary.
    Checks if the key "Eve" does not exist in the dictionary.
Check the test case for the output format!
'''

name = ['Alice', 'Bob', 'Charlie']
grades = {'Alice': 85, 'Bob': 90, 'Charlie': 78}

result = 'Alice is in the list.' if 'Alice' in name else 'Alice is not in the list.'
print(result)

result = 'David is in the list.' if "David" in name else "David is not in the list."
print(result)

result = 'Bob is in the dictionary.' if 'Bob' in grades else "Bob is not in the dictionary."
print(result)

result = "Eve is in the dictionary." if "Eve" in grades else "Eve is not in the dictionary."
print(result)