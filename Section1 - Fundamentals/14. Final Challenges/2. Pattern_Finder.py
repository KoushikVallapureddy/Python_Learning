'''
Pattern Finder:

#Challenge:

Create a function named find_occurrences that:

    1. Takes two string arguments: text and pattern
    2. Counts how many times pattern appears in text, including overlapping occurrences
    3. Returns a tuple containing:
        A boolean indicating if the pattern was found (True/False)
        The number of occurrences of the pattern
        A list of starting positions where the pattern was found
For example, if text is "abababab" and pattern is "aba", your function should return (True, 3, [0, 2, 4]), since "aba" appears at positions 0, 2, and 4.
    If the pattern is not found, return (False, 0, []).
'''

def find_occurrences(text, pattern):
    occurrences = []
    count = 0
    start = 0

    while True:
        start = text.find(pattern, start)
        if start == -1:
            break
        occurrences.append(start)
        count += 1
        start += 1
    found = count > 0
    return (found, count, occurrences)
text = input()
pattern = input()
result = find_occurrences(text, pattern)
print(result)
    
