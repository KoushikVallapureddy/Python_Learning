from directory import Directory

class FileSystem:
    """Represents the overall file system.
    
    This class serves as a facade for working with the file system components.
    """
    
    def __init__(self):
        self.root = Directory("root")
    
    def _get_directory_from_path(self, path):
        """Helper method to navigate to a directory from a path."""
        if not path or path == "/":
            return (None, self.root)

        parts = [p for p in path.split("/") if p]
        current = self.root
        for part in parts[:-1]:
            comp = current.get_component(part)
            if comp is None or not isinstance(comp, Directory):
                raise ValueError(f"Invalid path: {path}")
            current = comp

        target = current.get_component(parts[-1])
        if target is None:
            raise ValueError(f"Path not found: {path}")
        return (current, target)
    
    def add_to_path(self, path, component):
        """Adds a component at the specified path."""
        if not path or path == "/":
            self.root.add(component)
        else:
            parts = [p for p in path.split("/") if p]
            parent_dir = self.root
            for part in parts:
                comp = parent_dir.get_component(part)
                if comp is None or not isinstance(comp, Directory):
                    raise ValueError(f"Invalid path: {path}")
                parent_dir = comp
            parent_dir.add(component)
    
    def remove_from_path(self, path):
        """Removes a component at the specified path."""
        if not path or path == "/":
            raise ValueError("Cannot remove root directory")

        parent, target = self._get_directory_from_path(path)
        if target:
            parent.remove(target)
        else:
            raise ValueError(f"Path not found: {path}")
    
    def get_from_path(self, path):
        """Retrieves a component at the specified path."""
        if not path or path == "/":
            return self.root
        _, target = self._get_directory_from_path(path)
        return target
    
    def display(self):
        """Displays the entire file system."""
        return self.root.display()
    
    def get_total_size(self):
        """Returns the total size of all files in the system."""
        return self.root.get_size()