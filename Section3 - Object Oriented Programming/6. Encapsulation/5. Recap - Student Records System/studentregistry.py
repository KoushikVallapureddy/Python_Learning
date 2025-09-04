from student import Student

class StudentRegistry:
    def __init__(self):
        self.__students = {}
    
    def add_student(self, student):
        self.__students[student.id] = student
    
    def remove_student(self, student_id):
        if student_id in self.__students:
            del self.__students[student_id]
    
    def get_student(self, student_id):
        return self.__students.get(student_id)
    
    def get_top_student(self):
        if not self.__students:
            return None
        return max(self.__students.values(), key=lambda student: student.grade_average)
    
    def display_all(self):
        for student_id, student in self.__students.items():
            print(f"ID: {student_id}, Name: {student.name}, Average: {student.grade_average:.2f}")