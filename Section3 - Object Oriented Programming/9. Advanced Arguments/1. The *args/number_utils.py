def sum_all_numbers(*args):
    if not args:
        return 0

    for arg in args:
        if not isinstance(arg, (int, float)):
            print("Error: All arguments must be numbers")
            return None

    return sum(args)