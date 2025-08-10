'''
FizzBuzz is a simple and classic programming game often used to teach basic logic and control flow. 
The game involves iterating through numbers from 1 up to a specified limit. For each number:
    If the number is divisible by 3, the program outputs "Fizz."
    If the number is divisible by 7, it outputs "Buzz."
    If the number is divisible by both 3 and 7, it outputs "FizzBuzz."
    Otherwise, it simply outputs the number.
This game is an excellent way to practice using loops, conditionals, and modular arithmetic.

'''

#Challenge1
'''
For starters, just output the welcome message:
    Welcome to FizzBuzz!
'''
print('Welcome to FizzBuzz!')

#Challenge2:
'''
Add a function named fizzbuzz that gets one number (int) as an argument, and:

    If the number is divisible by 3, return "Fizz".
    If the number is divisible by 7, return "Buzz".
    If the number is divisible by both 3 and 7, return "FizzBuzz".
    If none of the above conditions are met, return the number itself in a string format.

After the function:
    Get input and cast it to int
    Call the function fizzbuzz with the input number
    Print the output of the function
'''

#Challenge3:
'''
Looping the numbers:
Everything is ready, let's play the game!
#Challenge:
Loop over the numbers from 1 to the number that the user entered, 
and each time use the function you created to calculate the FizzBuzz result and output it.
For example, for input of 7 output:
Welcome to FizzBuzz!
1
2
Fizz
4
5
Fizz
Buzz

'''

#Challenge4:
'''
Adding a Twist to the game:
Numbers that contain the digit "3" but aren't divisible by 3 or 7 will output Almost Fizz
To check if a string contains a char use 'in' for instance, "a" in word, note that you must cast the number to string for it work use str(num)
'''

def fizzbuzz(n):
    if n % 3 == 0:
        if n % 7 == 0:
            return "FizzBuzz"
        return 'Fizz'
    elif n % 7 == 0:
        return 'Buzz'
    elif "3" in str(n) and (n % 3 != 0 or n % 7 != 0):
        return "Almost Fizz"
    else:
        return str(n)

a = int(input())

for i in range(1, a + 1):
    print(fizzbuzz(i))
    


