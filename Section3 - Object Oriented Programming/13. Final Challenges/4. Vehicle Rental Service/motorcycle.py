# TODO: Import the Vehicle class from vehicle.py
from vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, vin, make, model, daily_rate, engine_size):
        super().__init__(vin, make, model, daily_rate)
        self.engine_size = engine_size
    
    def __str__(self):
        base_str = super().__str__()
        return f"Motorcycle: {base_str} - {self.engine_size}cc"