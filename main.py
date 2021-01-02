from student import Student
from courses import Courses

# define some Students
student_1 = Student("Robert", 22, "Piatra Neamt", "Informatica", "B5")
student_2 = Student("Vali", 22, "Piatra Neamt", "LPS", "A3")

# disciplines
mathematics = [student_1, student_2]
physics = [student_1]
informatics = [student_2]


# set students to courses
courses_school = Courses()
courses_school.set_students_courses(mathematics, physics, informatics)
courses_school.print_students_courses()
