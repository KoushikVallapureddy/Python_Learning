class Rental:
    def __init__(self, rental_id, vehicle, customer_name, days):
        # Initialize properties
        self.rental_id = rental_id
        self.vehicle = vehicle
        self.customer_name = customer_name
        self.days = days
        self.is_active = True
    
    def calculate_cost(self):
        return self.vehicle.daily_rate * self.days
    
    def end_rental(self):
        if self.is_active:
            self.is_active = False
            self.vehicle.end_rental()
            return True
        return False
    
    def __str__(self):
        status = "Active" if self.is_active else "Completed"
        return f"Rental {self.rental_id}: {self.vehicle.make} {self.vehicle.model} for {self.customer_name} - {status}"