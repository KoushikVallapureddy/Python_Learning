'''
Modifying Dictionaries:

Dictionaries in Python are not static; you can modify them after they are created. 
You can add new key-value pairs, update existing ones, or delete them.

Adding a new key-value pair:
    # Start with an empty dictionary
    my_dict = {}
    # Add a new key-value pair
    my_dict["name"] = "Alice"
    my_dict["age"] = 30
    print(my_dict)
    # Output: {'name': 'Alice', 'age': 30}

Updating an existing value:
    # Update the age
    my_dict["age"] = 31
    print(my_dict)
    # Output: {'name': 'Alice', 'age': 31}

Deleting a key-value pair:
    # Delete the age
    del my_dict["age"]
    print(my_dict)
    # Output: {'name': 'Alice'}

In these examples, we first add a new key-value pair to an empty dictionary. 
Then, we update the value of an existing key. Finally, we delete a key-value pair using the del keyword.
'''

