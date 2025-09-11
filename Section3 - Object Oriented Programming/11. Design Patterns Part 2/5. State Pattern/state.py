class State:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    def display_info(self):
        print(f"State: {self._name}")