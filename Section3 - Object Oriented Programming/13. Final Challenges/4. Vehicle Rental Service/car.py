from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, vin, make, model, daily_rate, passenger_capacity):
        super().__init__(vin, make, model, daily_rate)
        self.passenger_capacity = passenger_capacity
    
    def __str__(self):
        base_str = super().__str__()
        return f"Car: {base_str} - Seats {self.passenger_capacity}"
