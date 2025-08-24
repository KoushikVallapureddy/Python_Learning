'''
Recap - Number Processor:
Create function named process_numbers that takes a list of numbers and processes them according to specific rules.

Requirements:
    First filter out all negative numbers and zero
    Then for the remaining positive numbers:
        Double even numbers
        Triple odd numbers
Use map() and filter() to solve the problem.
'''

def process_numbers(numbers):
    positives = filter(lambda n: n > 0, numbers)
    processed = map(lambda n: n * 2 if n % 2 == 0 else n * 3, positives)
    return list(processed)

numbers = [1, 2, 3, 4]
print(process_numbers(numbers))