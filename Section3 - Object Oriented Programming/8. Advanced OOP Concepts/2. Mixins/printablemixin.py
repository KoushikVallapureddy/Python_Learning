class PrintableMixin:
    def print_details(self):
        return f"Product: {self.name}, Price: ${self.price}"