'''
List Casting:

You can use the list() function to cast iterables like tuples, strings, or ranges into lists. This is useful for working with elements in a modifiable format.

Casting a tuple to a list:
    my_tuple = (1, 2, 3)
    my_list = list(my_tuple)
    print(my_list)  # [1, 2, 3]

Casting a string splits it into individual characters:
    my_string = "hello"
    my_list = list(my_string)
    print(my_list)  # ['h', 'e', 'l', 'l', 'o']

Casting a range to a list gives all the numbers at once:
    my_range = range(5)
    my_list = list(my_range)
    print(my_list)  # [0, 1, 2, 3, 4]
    
You can also cast to other types like set or dict, but you’ll explore those later. For now, focus on list() to handle and transform data flexibly!
'''