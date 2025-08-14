'''
Basic Operations:
Sets come with built-in operations that allow you to perform common set-related tasks efficiently. These operations include adding elements, removing elements, and checking for the presence of elements.

Adding an element to a set:
    my_set = {1, 2, 3}
    my_set.add(4)
    print(my_set)
    # Output: {1, 2, 3, 4}

Removing an element from a set: (raises an error if it does not exist!)
    my_set = {1, 2, 3}
    my_set.remove(2)
    print(my_set)
    # Output: {1, 3}

Checking for the presence of an element:    
    my_set = {1, 2, 3}
    print(2 in my_set)
    # Output: True
    print(4 in my_set)
    # Output: False
'''