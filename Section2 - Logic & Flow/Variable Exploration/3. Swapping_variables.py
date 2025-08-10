'''
Swapping Variables:

Swapping variables is a common operation where the values of two variables are exchanged. 
Python offers a simple and elegant way to swap variables without needing a temporary variable, unlike many other programming languages.

Traditional Method (Using a Temporary Variable):
    a = 10
    b = 20
    temp = a
    a = b
    b = temp
    print(a)  # Output: 20
    print(b)  # Output: 10

Pythonic Way (Simultaneous Assignment):
    a = 10
    b = 20
    a, b = b, a
    print(a)  # Output: 20
    print(b)  # Output: 10

In the Pythonic way, the values of b and a are simultaneously assigned to a and b, respectively. 
This approach is more readable and doesn't require any additional variables.
'''