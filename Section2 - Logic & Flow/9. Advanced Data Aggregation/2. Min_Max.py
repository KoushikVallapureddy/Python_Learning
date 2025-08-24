'''
Finding Minimum and Maximum:

Python offers built-in functions to find the minimum and maximum values in a collection of data, such as a list or a tuple. 
These functions, min() and max(), are straightforward to use and can be applied to various data types, including numbers and strings.

Finding the Minimum Value:
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    smallest = min(numbers)
    print(smallest)
    # Output: 1
In this example, the min() function finds the smallest number in the numbers list.

Finding the Maximum Value:
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    largest = max(numbers)
    print(largest)
    # Output: 9
Here, the max() function finds the largest number in the numbers list.

Working with Strings:

The min() and max() functions can also be used with strings. 
In this case, they compare the strings based on their lexicographical order (i.e., the order they would appear in a dictionary).
    words = ["apple", "banana", "cherry"]
    smallest_word = min(words)
    largest_word = max(words)
    print(smallest_word)
    # Output: apple
    print(largest_word)
    # Output: cherry
In this example, min() returns "apple" because it comes first alphabetically, and max() returns "cherry" because it comes last alphabetically.

'''

#Challenge1:
'''
You are given a list of numbers and a list of words. Your task is to write a program that:
    Finds and prints the smallest and largest number in the list of numbers using min() and max().
    Finds and prints the smallest and largest word in the list of words based on their lexicographical order.
Check the test cases for output format
'''
numbers = [42, 17, 23, 56, 9, 34]
words = ["kiwi", "apple", "banana", "cherry", "date"]

print(f'Smallest number:',min(numbers))
print(f'Largest number:',max(numbers))
print(f'Smallest word:',min(words))
print(f'Largest word:',max(words))


#Challenge2:
'''
You are given two lists: temperatures containing daily temperatures in Fahrenheit, and humidity containing daily humidity percentages. 
Your task is to write a program that:
    Finds and prints the highest and lowest temperature from the temperatures list using max() and min().
    Finds and prints the highest and lowest humidity from the humidity list using max() and min().
Check the test cases for output format
'''
temperatures = [72, 68, 75, 80, 65, 70, 78]
humidity = [60, 55, 65, 70, 50, 58, 62]
print(f'Highest temperature: {max(temperatures)}°F')
print(f'Lowest temperature: {min(temperatures)}°F')
print(f'Highest humidity: {max(humidity)}%')
print(f'Lowest humidity: {min(humidity)}%')