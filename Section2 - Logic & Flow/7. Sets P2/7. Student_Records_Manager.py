'''
Student Records Manager:
The Student Records Manager manages student data using dictionaries and sets. 
Each student record includes their name, age, grades, and courses. 
Key operations include adding students, updating grades, checking course enrollment, calculating average grades, listing students by course, and
filtering top students based on grade thresholds.

This project demonstrates the practical use of dictionaries for structured data, sets to handle duplicates, and advanced decision-making for
efficient data management. 
It’s a practical way to apply Python concepts in a real-world scenario.
'''
#Challenge1:
'''
Initialize an empty dictionary named student_records to store the details of all students. 
This dictionary will serve as the foundation for the project, where each student's name will be a key, and their details (age, grades, and courses) will be stored as a nested dictionary.
'''


#Challenge2:
'''
Create a function named add_student that takes three arguments: name (string), age (integer), and courses (a list of strings). 
The function should:
    1. Check if the student name already exists in the student_records dictionary. If it does, print "Student '<name>' already exists.".
    2. If the name does not exist, add it to student_records with age, an empty set for grades, and a set of courses.
    3. Print "Student '<name>' added successfully.".

Add the following block of code at the bottom of your code:
    add_student("Alice", 20, ["Math", "Physics"])
    add_student("Bob", 22, ["Biology", "Chemistry"])
    print(student_records)
'''


#Challenge3:
'''
Add Grade:
Create a function named add_grade that takes two arguments: name (string) and grade (integer). The function should:

1. Check if the student name exists in the student_records dictionary.
    If it does not exist, print "Student '<name>' not found.".
2. If the name exists, add the grade to the student's grades set.
3. Print "Grade <grade> added for student '<name>'.".
Add (replace) the following block of code at the bottom of your code:
    add_student("Alice", 20, ["Math", "Physics"])
    add_student("Bob", 22, ["Biology", "Chemistry"])
    add_grade("Alice", 90)
    add_grade("Alice", 85)
    add_grade("Bob", 75)
    add_grade("Charlie", 80)  # Non-existent student
    print(student_records)

'''
#Challenge1 Code
student_records = {}

#Challenge2 Code
def add_student(name, age, courses):
    if name in student_records:
        print(f"Student '{name}' already exists.")
    else:
        student_records[name] = {
            "age": age,
            "grades": set(),
            "courses": set(courses)
        }
        print(f"Student '{name}' added successfully.")
# Test cases as instructed
'''
add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
print(student_records)
(Replaced them with Challenge3 Test Cases. Refer Challenge3 Test Cases)
'''
#Challenge3:
def add_grade(name, grade):
    if name not in student_records:
        print(f"Student '{name}' not found.")
    else:
        student_records[name]["grades"].add(grade)
        print(f"Grade {grade} added for student '{name}'.")

# Test cases as instructed
add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Charlie", 80)  # Non-existent student
print(student_records)