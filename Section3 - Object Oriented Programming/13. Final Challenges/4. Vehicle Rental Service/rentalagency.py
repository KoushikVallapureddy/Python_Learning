class RentalAgency:
    def __init__(self, name):
        # Initialize properties
        self.name = name
        self.vehicles = {}  # Dictionary to store vehicles (key: VIN, value: Vehicle object)
        self.rentals = {}   # Dictionary to store rentals (key: rental_id, value: Rental object)
        self.next_rental_id = 1
    
    def add_vehicle(self, vehicle):
        self.vehicles[vehicle.vin] = vehicle
        return True
    
    def rent_vehicle(self, vin, customer_name, days):
        if vin not in self.vehicles:
            return None

        vehicle = self.vehicles[vin]
        if not vehicle.available:
            return None

        rental_id = f"R{self.next_rental_id}"
        self.next_rental_id += 1

        from rental import Rental
        rental = Rental(rental_id, vehicle, customer_name, days)
        vehicle.start_rental()
        self.rentals[rental_id] = rental

        return rental_id
    
    def return_vehicle(self, rental_id):
        if rental_id not in self.rentals:
            return False

        rental = self.rentals[rental_id]
        if not rental.is_active:
            return False

        return rental.end_rental()
    
    def available_vehicles(self):
        return [vehicle for vehicle in self.vehicles.values() if vehicle.available]