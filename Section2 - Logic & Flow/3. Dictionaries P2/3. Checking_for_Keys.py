'''
Chekcing for keys:
When working with dictionaries, you often need to check if a specific key exists. 
Python provides simple ways to check for the presence of keys in a dictionary.

Using the in keyword:
    my_dict = {'name': 'Alice', 'age': 30}

    # Check if 'name' is a key in the dictionary
    if 'name' in my_dict:
        print('Name exists in the dictionary')

    # Check if 'city' is a key in the dictionary
    if 'city' not in my_dict:
        print('City does not exist in the dictionary')

In this example, we use the in keyword to check if 'name' is one of the keys in my_dict. 
We also use not in to check if 'city' is not a key in the dictionary.

Using the keys() method:
    my_dict = {'name': 'Alice', 'age': 30}

    # Check if 'age' is in the list of keys
    if 'age' in my_dict.keys():
        print('Age exists in the dictionary')

Here, my_dict.keys() returns a list of all keys in the dictionary, and we use in to check if 'age' is in that list.
'''