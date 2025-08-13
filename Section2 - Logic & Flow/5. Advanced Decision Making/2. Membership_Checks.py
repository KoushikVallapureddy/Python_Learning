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