from person import Person
import re

# The class for a Student

class Student(Person):

    REGEX_EXPRESSION_CLASSROOM = "^[A-Z][0-9]$"

    def __init__(self, name: str, age: int, city: str, school: str, classroom: str):
        super().__init__(name, age, city)
        self.set_school(school)
        self.set_classroom(classroom)

    def set_school(self, school: str) -> bool:
        if re.search(Student.REGEX_EXPRESSION_LETTERS, school):
            self.school = school
            return True
        else:
            return False

    def get_school(self) -> str:
        return self.school

    def set_classroom(self, classroom: str) -> bool:
        if re.search(Student.REGEX_EXPRESSION_CLASSROOM, classroom):
            self.classroom = classroom
            return True
        else:
            return False

    def get_classroom(self) -> str:
        return self.classroom

    def print_student(self):
        print(f'name: {self.name}, age: {self.age}, city: {self.city}')
        print(f'school: {self.school}, classroom: {self.classroom}')

    def __str__(self):
        return f'Student({self.name}, {self.school}, {self.classroom})'
