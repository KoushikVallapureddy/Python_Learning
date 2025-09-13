class Vehicle:
    def __init__(self, vin, make, model, daily_rate):
        # Initialize properties
        self.vin = vin
        self.make = make
        self.model = model
        self.daily_rate = daily_rate
        self.available = True
    
    def start_rental(self):
        if self.available:
            self.available = False
            return True
        return False
    
    def end_rental(self):
        self.available = True
        return True
    
    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"{self.make} {self.model} (VIN: {self.vin}) - {status}"