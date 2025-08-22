'''
Recursive Function Part2:

Recursive functions typically have two parts:
    Base Case: Defines when the recursion should stop.
    Recursive Step: Calls the function itself with smaller input.

Example: Calculating factorial using recursion:
    def factorial(n):
        if n == 1:  # Base case
            return 1
        return n * factorial(n - 1)  # Recursive call
    print(factorial(5))  # Output: 120
Here, the function keeps calling itself with n - 1 until it reaches 1, where the recursion stops.

Example: Reversing a String:
    def recursive_reverse(s):
        if len(s) <= 1:  # Base case: empty or single-character string
            return s
        else:
            return recursive_reverse(s[1:]) + s[0]  # Recursive step
    text = "hello"
    result = recursive_reverse(text)
    print(result)
    # Output: olleh
In this example, the recursive_reverse function calls itself with the rest of the string (s[1:]) until the string is empty or has only one character. Each call appends the first character to the result of the recursive call, effectively reversing the string.


'''

#Challenge1:
'''
Write a recursive function named fibonacci that takes a positive integer n as an argument and returns the nth Fibonacci number.
The Fibonacci sequence is defined as:
    fibonacci(1) = 0
    fibonacci(2) = 1
    fibonacci(n) = fibonacci(n-1) + fibonacci(n-2) for n > 2.

Example Input:
    n = 6

Example Output:
    5


def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))
'''



#Challenge2:
'''
Write a recursive function named sum_digits that takes a positive integer n as an argument and returns the sum of its digits. 
The function should work as follows:
    If n is a single digit (less than 10), return that digit.
    Otherwise, return the sum of the last digit of n and the result of sum_digits called with n divided by 10 (integer division).

Example Input:
    n = 1234
Example Output:
    10
Explanation: 1 + 2 + 3 + 4 = 10
You can use the special operator // to calculate the floor division, for example: 3 // 2 = 1
'''
def sum_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)
    
n = int(input())
print(sum_digits(n))