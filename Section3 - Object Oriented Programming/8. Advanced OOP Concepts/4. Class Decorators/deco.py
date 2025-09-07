def add_counter(cls):
    # TODO: Initialize the call_counts dictionary with keys "add" and "subtract" both starting at 0
    cls.call_counts = {"add": 0, "subtract": 0}
    
    # TODO: Store original methods
    # Store the original add method from the class
    original_add = cls.add
    
    # Store the original subtract method from the class
    original_subtract = cls.subtract
    
    # TODO: Define wrapped methods that increment counters and preserve original functionality
    def wrapped_add(self, a, b):
        self.__class__.call_counts["add"] += 1
        return original_add(self, a, b)
    
    def wrapped_subtract(self, a, b):
        self.__class__.call_counts["subtract"] += 1
        return original_subtract(self, a, b)
    
    # TODO: Replace original methods with wrapped versions
    cls.add = wrapped_add
    cls.subtract = wrapped_subtract
    
    # TODO: Return the modified class
    return cls