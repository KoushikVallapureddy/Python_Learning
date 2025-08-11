'''
Looping Through Dictionaries:
Looping through a dictionary allows you to access each key-value pair and perform operations on them. 
Python provides several ways to iterate through dictionaries, making it easy to work with their contents.
Looping thrrough keys:
    my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

    for key in my_dict:
        print(key)
Output:
    name
    age
    city    

Looping through values:
    for value in my_dict.values():
        print(value)
Output:
    Alice
    30
    New York

Looping through key-value pairs:
    for key, value in my_dict.items():
        print(f'{key}: {value}')
Output:
    name: Alice
    age: 30
    city: New York
    
In these examples, the first loop iterates over the keys of the dictionary. 
The second loop iterates over the values using the values() method. 
The third loop uses the items() method to iterate over both keys and values simultaneously.
'''
