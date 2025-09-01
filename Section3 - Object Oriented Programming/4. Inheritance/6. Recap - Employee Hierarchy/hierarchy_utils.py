def show_hierarchy(cls):
    print(f"Class hierarchy for {cls.__name__}:")
    for c in cls.__mro__:
        print(c.__name__)