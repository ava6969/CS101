
class Student:

    def __init__(self, name, age, height):

        self.name = name
        self.age = age
        self.height = height

    def study(self):
        print(self.name, 'is studying')


class HighSchoolStudent(Student):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
