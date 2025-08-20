'''
Lambda functions are incredibly useful with the sorted() function to customize sorting in different scenarios. Here are a few examples:

Sorting Strings by Length:
    names = ["Alice", "Bob", "Charlie", "Diana"]
    sorted_names = sorted(names, key=lambda x: len(x))
    print(sorted_names)
    # Output: ['Bob', 'Alice', 'Diana', 'Charlie']

Sorting Dictionaries by Values:
    grades = {"Alice": 85, "Bob": 90, "Charlie": 78}
    sorted_grades = sorted(grades.items(), key=lambda x: x[1])
    print(sorted_grades)
    # Output: [('Charlie', 78), ('Alice', 85), ('Bob', 90)]

Sorting Numbers by Absolute Value:
    numbers = [-10, 15, -20, 25]
    sorted_numbers = sorted(numbers, key=lambda x: abs(x))
    print(sorted_numbers)
    # Output: [-10, 15, -20, 25]

Sorting Tuples by Multiple Criteria:
    data = [("Alice", 25), ("Bob", 30), ("Charlie", 25)]
    sorted_data = sorted(data, key=lambda x: (x[1], x[0]))
    print(sorted_data)
    # Output: [('Alice', 25), ('Charlie', 25), ('Bob', 30)]

'''