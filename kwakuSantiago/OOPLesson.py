
class ClassTemplate:

    def __init__(self, newName, newAge, newGrade):
        # Attributes
        self.name = newName
        self.age = newAge
        self.grade = newGrade
        color = "red"

    def change_name(self, newName):
        self.name = newName

    def change_age(self, newAge):
        self.age = newAge

    def __repr__(self):
        # return "[name: " + self.name + "," + self.age + " " + " ]"
        return "name: {} age: {} grade: {}".format(self.name, self.age, self.grade)


morfin = ClassTemplate("MORFIN", 18, 'A')
print(morfin)