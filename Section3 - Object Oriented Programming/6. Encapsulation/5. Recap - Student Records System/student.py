class Student:
    def __init__(self, student_id, name, enrolled=True):
        self.__id = student_id
        self.__grades = {}
        self.__enrolled = enrolled
        self.name = name  # use setter for validation
    
    # ID property (read-only)
    @property
    def id(self):
        return self.__id
    
    # Name property with getter and setter
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError("Name must be at least 2 characters long")
        self.__name = value
    
    # Enrolled property with getter and setter
    @property
    def enrolled(self):
        return self.__enrolled
    
    @enrolled.setter
    def enrolled(self, value):
        if not isinstance(value, bool):
            raise ValueError("Enrolled must be a boolean value")
        self.__enrolled = value
    
    # Grade average property (read-only)
    @property
    def grade_average(self):
        if not self.__grades:
            return 0
        return sum(self.__grades.values()) / len(self.__grades)
    
    # Methods
    def add_grade(self, course, grade):
        self.__grades[course] = grade
    
    def display_record(self):
        enrolled_status = "Yes" if self.__enrolled else "No"
        print(f"ID: {self.__id}")
        print(f"Name: {self.__name}")
        print(f"Enrolled: {enrolled_status}")
        print(f"Courses: {len(self.__grades)}")
        print(f"Grade Average: {self.grade_average:.2f}")