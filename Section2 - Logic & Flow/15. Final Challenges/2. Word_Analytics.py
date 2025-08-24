'''
Create a function named analyze_text that analyzes words in a text string.

Your function should:
    Count unique words (case-insensitive)
    Find all words that appear more than once
    Identify all palindrome words (words that read the same forwards and backwards, like "level")

Return a dictionary with three keys:
    unique_count: the number of unique words (count also repeated words once each)
    repeated_words: a sorted list of words appearing more than once
    palindromes: a sorted list of palindrome words

Notes:
    Treat words as case-insensitive (e.g., "Hello" and "hello" are the same word)
    Remove any punctuation (.,!?:;"()) from words
    Sort both the repeated_words and palindromes lists alphabetically

Example Input:

"Madam saw a racecar. Dad said hello hello to mom."

Expected Output:

{
    'unique_count': 9,
    'repeated_words': ['hello'],
    'palindromes': ['a', 'dad', 'madam', 'mom', 'racecar']
}
'''

def analyze_text(text):
    import string

    text = text.lower()
    for p in string.punctuation:
        text = text.replace(p, "")

    words = text.split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    unique_count = len(word_counts)
    repeated_words = sorted([w for w, c in word_counts.items() if c > 1])
    palindromes = sorted([w for w in set(words) if w == w[::-1]])

    return {
        "unique_count": unique_count,
        "repeated_words": repeated_words,
        "palindromes": palindromes
    }

text = 'Wow! Did Hannah see that Race car? Mom was there too. Hannah did see it!'
print(analyze_text(text))
