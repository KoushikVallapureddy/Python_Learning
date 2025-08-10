'''
Dictionary Methods:

Dictionaries, just like lists, come equipped with a variety of built-in methods to perform common operations. 
These methods can help you manipulate dictionaries more efficiently. Let's explore some of the key methods:

keys(): Returns a view object that displays a list of all the keys in the dictionary.
    my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
    keys = my_dict.keys()
    print(keys)
    # Output: dict_keys(['name', 'age', 'city'])

values(): Returns a view object that displays a list of all the values in the dictionary.
    values = my_dict.values()
    print(values)
    # Output: dict_values(['Alice', 30, 'New York'])

items(): Returns a view object that displays a list of a dictionary's key-value tuple pairs.
    items = my_dict.items()
    print(items)
    # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])

get(key, default): Returns the value for the specified key. If the key is not found, it returns the default value (or None if no default is specified).
    age = my_dict.get('age')
    print(age)
    # Output: 30
    country = my_dict.get('country', 'USA')
    print(country)
    # Output: USA

pop(key): Removes the element with the specified key and returns its value.
    city = my_dict.pop('city')
    print(city)
    # Output: 'New York'
    print(my_dict)
    # Output: {'name': 'Alice', 'age': 30}
'''