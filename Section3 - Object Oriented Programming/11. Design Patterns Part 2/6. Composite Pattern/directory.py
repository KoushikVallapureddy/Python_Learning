from file_system_component import FileSystemComponent

class Directory(FileSystemComponent):
    """Represents a directory in the file system.
    
    This class serves as the 'Composite' in the Composite pattern.
    """
    
    def __init__(self, name):
        super().__init__(name)
        self._components = []
    
    def get_size(self):
        return sum(component.get_size() for component in self._components)
    
    def display(self, indent=0):
        result = [" " * indent + f"Directory: {self.name} ({self.get_size()} KB)"]
        for component in self._components:
            result.append(component.display(indent + 2))
        return "\n".join(result)
    
    def add(self, component):
        if any(c.name == component.name for c in self._components):
            raise ValueError(f"Component with name '{component.name}' already exists")
        self._components.append(component)
    
    def remove(self, component):
        if component in self._components:
            self._components.remove(component)
        else:
            raise ValueError(f"Component {component.name} not found")
    
    def get_component(self, name):
        for c in self._components:
            if c.name == name:
                return c
        return None
    
    def find_component_recursive(self, name):
        """Recursively searches for a component with the given name."""
        found = self.get_component(name)
        if found:
            return found
        for component in self._components:
            if isinstance(component, Directory):
                found = component.find_component_recursive(name)
                if found:
                    return found
        return None