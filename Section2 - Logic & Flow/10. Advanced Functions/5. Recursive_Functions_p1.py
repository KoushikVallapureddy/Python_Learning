'''
Recursive Function Part1:

A recursive function is a function that calls itself to solve smaller instances of a problem. Each recursive call must bring the function closer to a base case, which stops the recursion.

Example: Summing numbers from 1 to n:
    def sum_to_n(n):
        if n == 0:  # Base case
            return 0
        return n + sum_to_n(n - 1)  # Recursive step
    print(sum_to_n(5))  # Output: 15
'''

#Challenge1:
'''
Write a recursive function named count_down that takes a positive integer n as an argument and prints each number from n down to 0.
'''
def count_down(n):
    if n < 0:
        return
    print(n)
    count_down(n-1)

n = int(input())
count_down(n)


#Challenge2:
'''
Write a recursive function named print_sequence that takes a positive integer n as an argument and prints a countdown sequence. 
For each number from n to 1, it should print 'T-minus {number}'. 
When it reaches 0, it should print 'Blast off!'. For example, if n is 3, the output should be:
    T-minus 3
    T-minus 2
    T-minus 1
    Blast off!
'''

def print_sequence(n):
    if n == 0:
        print('Blast off!')
        return
    print(f'T-minus',n)
    print_sequence(n-1)


n = int(input())
print_sequence(n)