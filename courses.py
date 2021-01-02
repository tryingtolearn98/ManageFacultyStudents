from student import Student


'''
In this class we will have the logic for the courses.
'''

class Courses():

    def __init__(self):
        self.all_courses = {'Mathematics': [],
                            'Informatics': [], 'Physics': []}

    def set_students_courses(self, *students_lists: Student) -> bool:
        for index, student_list in enumerate(students_lists):
            for student in student_list:
                if isinstance(student, Student):
                    if index == 0:
                        self.all_courses['Mathematics'].append(student)
                    elif index == 1:
                        self.all_courses['Informatics'].append(student)
                    elif index == 2:
                        self.all_courses['Physics'].append(student)

    def print_students_courses(self):
        for key in self.all_courses:
            print(f'{key} : {[str(student) for student in self.all_courses[key]]}')
