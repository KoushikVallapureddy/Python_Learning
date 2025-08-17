'''
Recap - Tournament Tracker

In a competitive gaming tournament, players participate in different matches. 
Your task is to analyze player participation across three matches using Python sets.

You'll be given three sets of players:
    match1: Players who participated in Match 1
    match2: Players who participated in Match 2
    match3: Players who participated in Match 3

Your task is to:
    1. Find players who participated in all three matches
    2. Identify players who participated in exactly two matches
    3. Determine players who participated in only one match
    4. Count the total number of unique players in the tournament
    5. Find players who participated in Match 1 but not in Match 2 or Match 3

Print the results in the following format:
    Use sorted(list(set_name)) to display players in alphabetical order
    Print the exact output format shown in the example

Example Input:
    {"Alice", "Bob", "Charlie", "Diana"}
    {"Charlie", "Diana", "Eve", "Frank"}
    {"Alice", "Diana", "Frank", "George"}

Example Output:
    Players in all matches: ['Diana']
    Players in exactly two matches: ['Alice', 'Charlie', 'Frank']
    Players in only one match: ['Bob', 'Eve', 'George']
    Total unique players: 7
    Players in Match 1 only: ['Bob']


'''

# Read input for the three matches
match1 = eval(input())
match2 = eval(input())
match3 = eval(input())

# 1. Find players who participated in all three matches
all_matches = match1 & match2 & match3

# 2. Find players who participated in exactly two matches
exactly_two = ((match1 & match2) | (match2 & match3) | (match1 & match3)) - (match1 & match2 & match3)

# 3. Find players who participated in only one match
only_one = (match1 ^ match2 ^ match3) - exactly_two
only_one = (
    (match1 - match2 - match3) |
    (match2 - match1 - match3) |
    (match3 - match1 - match2)
)

# 4. Count total unique players
unique_players = match1 | match2 | match3
count = len(unique_players)

# 5. Find players in Match 1 only
match1_only = match1 - match2 - match3

# Print results in the specified format
print("Players in all matches:", sorted(list(all_matches)))
print('Players in exactly two matches:', sorted(list(exactly_two)))
print('Players in only one match:', sorted(list(only_one)))
print('Total unique players:' ,count)
print('Players in Match 1 only:', sorted(list(match1_only)))