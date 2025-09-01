from person import Person
class Employee(Person):
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.job = job
    
    def introduce(self):
        super().introduce()
        print(f"I work as a {self.job}")