class Temperature:
    celsius_readings = []
    
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9 / 5 + 32
    
    @classmethod
    def add_reading(cls, celsius):
        cls.celsius_readings.append(celsius)
    
    @classmethod
    def average_reading(cls):
        if not cls.celsius_readings:
            return 0
        return sum(cls.celsius_readings) / len(cls.celsius_readings)