class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
        
    def detach(self, observer):
        self._observers.remove(observer)
        
    def notify(self, data):
        for observer in self._observers:
            observer.update(data)
            
class Observer:
    def update(self, data):
        pass


class WeatherStation(Subject):
    def __init__(self):
        super().__init__()
        self._temperature = None

    def set_temperature(self, temperature):
        self._temperature = temperature
        self.notify(self._temperature)


class WeatherDisplay(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, data):
        print(f"{self.name} display: Current temperature is {data}°C")

