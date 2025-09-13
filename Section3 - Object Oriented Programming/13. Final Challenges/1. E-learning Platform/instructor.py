from course import Course

class Instructor:
    def __init__(self, name, email, expertise):
        self.name = name
        self.email = email
        self.expertise = expertise
        self.courses = []
    
    
    def assign_to_course(self, course):
        course.assign_instructor(self)
        self.courses.append(course)
        return True