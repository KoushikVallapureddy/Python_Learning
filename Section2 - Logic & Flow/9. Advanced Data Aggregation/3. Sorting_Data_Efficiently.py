'''
Sorting Data Efficiently:

Sorting is a fundamental operation in computer science, and Python offers powerful built-in tools to sort data efficiently. 
The primary function for sorting is sorted(), which can be used to sort various types of data, including numbers, strings, and more complex objects.

Basic Sorting:

The sorted() function takes an iterable (e.g., a list, tuple, or set) as its argument and returns a new list containing the sorted elements. By default, it sorts in ascending order.
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    sorted_numbers = sorted(numbers)
    print(sorted_numbers)
    # Output: [1, 1, 2, 3, 4, 5, 6, 9]
In this example, sorted() sorts the numbers list in ascending order.

Reverse Sorting:

To sort in descending order, you can use the reverse parameter and set it to True.
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    sorted_numbers_desc = sorted(numbers, reverse=True)
    print(sorted_numbers_desc)
    # Output: [9, 6, 5, 4, 3, 2, 1, 1]
Here, sorted() sorts the numbers list in descending order.

Sorting Strings:

The sorted() function can also sort strings based on their lexicographical order (i.e., the order they would appear in a dictionary).
    words = ["apple", "banana", "cherry"]
    sorted_words = sorted(words)
    print(sorted_words)
    # Output: ['apple', 'banana', 'cherry']
In this example, sorted() sorts the words list in alphabetical order.

Custom Sorting with Key Function:

For more complex sorting needs, you can use the key parameter to specify a function that determines the sorting order. The key function is applied to each element before sorting, and the returned values are used for comparison.
    words = ["apple", "banana", "cherry"]
    sorted_words_by_length = sorted(words, key=len)
    print(sorted_words_by_length)
    # Output: ['apple', 'banana', 'cherry']
In this case, sorted() sorts the words list based on the length of each word, using the len() function as the key.
'''

#Challenge1:
'''
Write a program that performs the following sorting tasks using the sorted() function:
    Sort a list of numbers in ascending order.
    Sort the same list of numbers in descending order.
    Sort a list of strings in alphabetical order.
    Sort the same list of strings based on their length.
'''

numbers = [5, 3, 8, 1, 2]
words = ["elephant", "cat", "dolphin", "bee"]

ascending_numbers = sorted(numbers)
descending_numbers = sorted(numbers, reverse=True)
alphabetical_words = sorted(words)
length_sorted_words = sorted(words, key=len)

print("Ascending:", ascending_numbers)
print("Descending:", descending_numbers)
print("Alphabetical:", alphabetical_words)
print("By Length:", length_sorted_words)

#Challenge2:
'''
Create a function named analyze_grades that takes a dictionary of student grades as an argument. 
The dictionary keys are student names, and the values are their corresponding grades. The function should perform the following operations:

    Calculate the average grade of all students.
    Find the highest and lowest grades.
    Identify the student(s) with the highest and lowest grades.
    Return a dictionary containing the following information:
        'average': The average grade (rounded to 2 decimal places)
        'highest': The highest grade
        'lowest': The lowest grade
        'top_student': The name of the student with the highest grade
        'bottom_student': The name of the student with the lowest grade

Test your function with the following dictionary:   
student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95, 'Eve': 88}
'''
def analyze_grades(grades):
    values = list(grades.values())
    average = round(sum(values) / len(values), 2)
    highest = max(values)
    lowest = min(values)
    # Find the first student with the highest and lowest grades
    top_student = [name for name, grade in grades.items() if grade == highest][0]
    bottom_student = [name for name, grade in grades.items() if grade == lowest][0]
    return {
        'average': average,
        'highest': highest,
        'lowest': lowest,
        'top_student': top_student,
        'bottom_student': bottom_student
    }

student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95, 'Eve': 88}
result = analyze_grades(student_grades)
print(result)
