from counter import Counter

# Comprehensive test case handler
test_case = input()

if test_case == "init_test":
    c = Counter()
    print(c)

elif test_case == "init_with_value":
    c = Counter(10)
    print(c)

elif test_case == "string_representation":
    c = Counter(5)
    print(c)

elif test_case == "addition":
    c = Counter(3) + 7
    print(c)

elif test_case == "chained_addition":
    c = Counter(1) + 2 + 3
    print(c)

elif test_case == "negative_values":
    c = Counter(-5)
    print(c)
    print(c + -3)

elif test_case == "zero_value":
    c = Counter(0) + 0
    print(c)

elif test_case == "large_values":
    c = Counter(1000000) + 9000000
    print(c)

elif test_case == "multiple_counters":
    counter1 = Counter(5)
    counter2 = Counter(10)
    print(counter1)
    print(counter2)

elif test_case == "type_validation":
    c = Counter(5) + 2.5
    print(c)