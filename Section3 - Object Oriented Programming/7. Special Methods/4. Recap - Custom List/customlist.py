class CustomList:
    def __init__(self, items=None):
        if items is None:
            self.items = []
        else:
            self.items = list(items)
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value
    
    def __str__(self):
        return str(self.items)
    
    def __repr__(self):
        return f"CustomList({self.items})"
    
    def __add__(self, other):
        if isinstance(other, CustomList):
            return CustomList(self.items + other.items)
        else:
            return CustomList(self.items + list(other))
    
    def __iter__(self):
        return iter(self.items)
    
    def __contains__(self, item):
        return item in self.items
    
    def append(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def clear(self):
        self.items.clear()