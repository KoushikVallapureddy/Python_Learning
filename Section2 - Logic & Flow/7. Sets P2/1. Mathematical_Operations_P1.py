'''
Mathematical Operations Part1:
Sets support mathematical operations such as union, intersection, difference, and symmetric difference. 
These operations are useful for comparing and combining sets in various ways.

Union (| or union()): Combines the elements from both sets, excluding duplicates.
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    union_set = set1 | set2
    print(union_set)
    # Output: {1, 2, 3, 4, 5}

Intersection (& or intersection()): Returns a set containing only the elements that are common to both sets.
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    intersection_set = set1 & set2
    print(intersection_set)
    # Output: {3}

Difference (- or difference()): Returns a set containing the elements that are in the first set but not in the second set.
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    difference_set = set1 - set2
    print(difference_set)
    # Output: {1, 2}

Symmetric Difference (^ or symmetric_difference()): Returns a set containing the elements that are in either of the sets, but not in both.
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    symmetric_difference_set = set1 ^ set2
    print(symmetric_difference_set)
    # Output: {1, 2, 4, 5}


'''