'''
A recursive function is a function that calls itself to solve smaller instances of a problem. Each recursive call must bring the function closer to a base case, which stops the recursion.

Example: Summing numbers from 1 to n:
    def sum_to_n(n):
        if n == 0:  # Base case
            return 0
        return n + sum_to_n(n - 1)  # Recursive step
    print(sum_to_n(5))  # Output: 15
'''