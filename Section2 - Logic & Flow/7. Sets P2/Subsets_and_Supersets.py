'''
Subsets and Supersets:
In set theory, a subset is a set where all its elements are contained within another set. 
Conversely, a superset is a set that contains all the elements of another set.

Checking for a subset (<= or issubset()):
    set1 = {1, 2}
    set2 = {1, 2, 3}
    is_subset = set1 <= set2
    print(is_subset)
    # Output: True
In this example, set1 is a subset of set2 because all elements of set1 are also in set2.

Checking for a proper subset (<):
    set1 = {1, 2}
    set2 = {1, 2, 3}
    is_proper_subset = set1 < set2
    print(is_proper_subset)
    # Output: True

Here, set1 is a proper subset of set2 because set1 is a subset of set2, and set2 contains at least one element not in set1.

Checking for a superset (>= or issuperset()):
    set1 = {1, 2, 3}
    set2 = {1, 2}
    is_superset = set1 >= set2
    print(is_superset)
    # Output: True
In this case, set1 is a superset of set2 because set1 contains all elements of set2.

Checking for a proper superset (>):
    set1 = {1, 2, 3}
    set2 = {1, 2}
    is_proper_superset = set1 > set2
    print(is_proper_superset)
    # Output: True
Here, set1 is a proper superset of set2 because set1 is a superset of set2, and set1 contains at least one element not in set2.
'''