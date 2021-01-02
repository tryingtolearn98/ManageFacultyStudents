import re

# The class for a Person

class Person:

    REGEX_EXPRESSION_LETTERS = "^[a-zA-Z\\s-]+$"

    def __init__(self, name: str, age: int, city: str):
        self.set_age(age)
        self.set_city(city)
        self.set_name(name)

    def set_age(self, age: int) -> bool:
        if age > 0 and age < 100:
            self.age = age
            return True
        else:
            return False

    def get_age(self) -> int:
        return self.age

    def set_city(self, city: str) -> bool:
        if re.search(Person.REGEX_EXPRESSION_LETTERS, city):
            self.city = city
            return True
        else:
            return False

    def get_city(self) -> str:
        return self.city

    def set_name(self, name: str) -> bool:
        if re.search(Person.REGEX_EXPRESSION_LETTERS, name):
            self.name = name
            return True
        else:
            return False
