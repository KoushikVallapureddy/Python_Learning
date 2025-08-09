'''
Sequence Operations:

Python provides several operators that can be used with sequences like lists, strings, and tuples.
Concatenation with the + operator joins two sequences together:
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    combined_list = list1 + list2
After executing the above code, combined_list contains:
    [1, 2, 3, 4, 5, 6]

Repetition with the * operator repeats a sequence a specified number of times:
    numbers = [1, 2, 3]
    repeated_numbers = numbers * 3
After executing the above code, repeated_numbers contains:
    [1, 2, 3, 1, 2, 3, 1, 2, 3]

These operators work with other sequences too:
    # String concatenation
    greeting = "Hello" + " " + "World"  # "Hello World"

    # String repetition
    stars = "*" * 5  # "*****"

'''

#Challenge1:
'''
Create a function named create_pattern that takes two arguments:
    A list of numbers (numbers).
    An integer (repeats).

The function should:

    Concatenate the list with itself (list + list).
    Repeat the resulting list repeats times using the * operator.
    Return the final pattern.


def create_pattern(numbers, repeats):
    combined_list = numbers + numbers
    repeating_list = combined_list * repeats
    print(repeating_list)
numbers = list((input().split(',')))
repeats = int(input())
create_pattern(numbers, repeats)

'''

#Challenge2:
'''
Create a program that receives a list of numbers as input and prints a new list that:

    Contains the original list followed by its reverse
    Has the first element of the original list inserted at the beginning and the last element inserted at the end
    Repeats this entire sequence twice

'''
numbers = input().split()
list1 = numbers[0]
list2 = numbers
list3 = numbers[::-1]
list4 = numbers[-1:]
total_list = [list1]+list2+list3+list4
final_list = total_list * 2
print(final_list)



