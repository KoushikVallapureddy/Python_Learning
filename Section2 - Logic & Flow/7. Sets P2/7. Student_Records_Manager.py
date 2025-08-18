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
#Challenge1: Empty Dictionary
'''
Initialize an empty dictionary named student_records to store the details of all students. 
This dictionary will serve as the foundation for the project, where each student's name will be a key, and their details (age, grades, and courses) will be stored as a nested dictionary.
'''


#Challenge2: Add Student
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


#Challenge3: Add Grade
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

#Challenge4: is enrolled
'''
Create a function named is_enrolled that takes two arguments: name (string) and course (string). The function should:

1. Check if the student name exists in the student_records dictionary.
    If it does not exist, print "Student '<name>' not found." and return False.

If the name exists, check if the course is in the student's courses set.
    If it is, return True.
    If not, return False.

Add (replace) the following block of code at the bottom of your code:
    add_student("Alice", 20, ["Math", "Physics"])
    add_student("Bob", 22, ["Biology", "Chemistry"])
    add_grade("Alice", 90)
    add_grade("Alice", 85)
    add_grade("Bob", 75)
    add_grade("Charlie", 80)  # Non-existent student
    print(is_enrolled("Alice", "Math"))  # Should return True
    print(is_enrolled("Alice", "Biology"))  # Should return False
    print(is_enrolled("Bob", "Biology"))  # Should return True
    print(is_enrolled("Charlie", "Math"))  # Non-existent student, should print message and return False

'''
#Challenge5: Average Grade
'''
Create a function named calculate_average_grade that takes one argument: name (string). The function should:

1. Check if the student name exists in the student_records dictionary.
    If it does not exist, print "Student '<name>' not found." and return None.
2. If the name exists, calculate the average of the grades in the student's grades set.
    If the grades set is empty, return 0.
    Otherwise, calculate and return the average grade as a float.

Add (replace) the following block of code at the bottom of your code:
    add_student("Alice", 20, ["Math", "Physics"])
    add_student("Bob", 22, ["Biology", "Chemistry"])
    add_grade("Alice", 90)
    add_grade("Alice", 85)
    add_grade("Bob", 75)
    print(calculate_average_grade("Alice"))  # Should return 87.5
    print(calculate_average_grade("Bob"))  # Should return 75.0
    print(calculate_average_grade("Charlie"))  # Non-existent student, should print message and return None
    print(calculate_average_grade("Alice"))  # Should return 87.5 again
'''
#Challenge6: List by Course
'''
Create a function named list_students_by_course that takes one argument: course (string). The function should:
    1. Iterate through the student_records dictionary and find all students enrolled in the specified course.
    2. Return a list of names of students who are enrolled in the course.
    3. If no students are enrolled in the course, return an empty list.

Add (replace) the following block of code at the bottom of your code:

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
print(list_students_by_course("Math"))  # Should return ["Alice", "Bob"]
print(list_students_by_course("Physics"))  # Should return ["Alice", "Diana"]
print(list_students_by_course("Biology"))  # Should return ["Bob"]
print(list_students_by_course("History"))  # Should return an empty list
'''

#Challenge7: Top Students
'''
Create a function named filter_top_students that takes one argument: threshold (float). The function should:

1. Iterate through the student_records dictionary and find all students whose average grade is greater than the specified threshold.
2. Use the calculate_average_grade function to get each student's average grade.
3. Return a list of names of the top students.
4. If no students meet the criteria, return an empty list.

Add (replace) the following block of code at the bottom of your code:
    add_student("Alice", 20, ["Math", "Physics"])
    add_student("Bob", 22, ["Math", "Biology"])
    add_student("Diana", 23, ["Chemistry", "Physics"])
    add_grade("Alice", 90)
    add_grade("Alice", 85)
    add_grade("Bob", 75)
    add_grade("Diana", 95)
    print(filter_top_students(80))  # Should return ["Alice", "Diana"]
    print(filter_top_students(90))  # Should return ["Diana"]
    print(filter_top_students(100))  # Should return an empty list

Take a moment to reflect on how you’ve combined dictionaries, sets, and decision-making to create a fully functional program. Great job! 🚀


'''

#Challenge1 Code
student_records = {}

#Challenge2 Code : Add Student
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
# Test cases as instructed (Replaced them with Challenge3 Test Cases. Refer Challenge3 Test Cases. To execute test cases #2 comments other test cases)
'''
add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
print(student_records)

'''

#Challenge3_Code: Add Grade
def add_grade(name, grade):
    if name not in student_records:
        print(f"Student '{name}' not found.")
    else:
        student_records[name]["grades"].add(grade)
        print(f"Grade {grade} added for student '{name}'.")

# Test cases as instructed (Replaced them with Challenge4 Test Cases. Refer Challenge4 Test Cases. To execute test cases #3 comments other test cases)
'''
add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Charlie", 80)  # Non-existent student
print(student_records)
'''


#Challenge4_Code: is_enrolled
def is_enrolled(name, course):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return False
    if course in student_records[name]["courses"]:
        return True
    else:
        return False

#Test cases as instructed (Replaced them with Challenge5 Test Cases. Refer Challenge4 Test Cases. To execute test cases #4 comments other test cases)
'''
add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Charlie", 80)  # Non-existent student
print(is_enrolled("Alice", "Math"))  # Should return True
print(is_enrolled("Alice", "Biology"))  # Should return False
print(is_enrolled("Bob", "Biology"))  # Should return True
print(is_enrolled("Charlie", "Math"))  # Non-existent student, should print message and return False
    
'''

#Challenge5_code: Average Grade
def calculate_average_grade(name):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return None
    grades = student_records[name]['grades']
    if not grades:
        return 0
    return sum(grades) / len(grades)

#Test cases as instructed (Replaced them with Challenge6 Test Cases. Refer Challenge5 Test Cases. To execute test cases #5 comments other test cases)
'''
add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
print(calculate_average_grade("Alice"))  # Should return 87.5
print(calculate_average_grade("Bob"))  # Should return 75.0
print(calculate_average_grade("Charlie"))  # Non-existent student, should print message and return None
print(calculate_average_grade("Alice"))  # Should return 87.5 again

'''

#Challenge6_Code: List by Course
def list_students_by_course(course):
    students_in_course = []
    for name, details in student_records.items():
        if course in details["courses"]:
            students_in_course.append(name)
    return students_in_course

#Test cases as instructed (Replaced them with Challenge7 Test Cases. Refer Challenge5 Test Cases. To execute test cases #6 comments other test cases)
'''
add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
print(list_students_by_course("Math"))  # Should return ["Alice", "Bob"]
print(list_students_by_course("Physics"))  # Should return ["Alice", "Diana"]
print(list_students_by_course("Biology"))  # Should return ["Bob"]
print(list_students_by_course("History"))  # Should return an empty list
'''

#Challenge7_Code: Top Students
def filter_top_students(threshold):
    top_students = []
    for name in student_records:
        avg = calculate_average_grade(name)
        if avg is not None and avg > threshold:
            top_students.append(name)
    return top_students

# Test cases as instructed
add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Diana", 95)
print(filter_top_students(80))  # Should return ["Alice", "Diana"]
print(filter_top_students(90))  # Should return ["Diana"]
print(filter_top_students(100))  # Should return an empty list


