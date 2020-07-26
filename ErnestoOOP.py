# oop

# attributes
# has_glasses, has_computer, class, age, name, class_grade

# behaviors
# speak() listen() walk()


class Student:

    def __init__(self, name, age, class_year, class_grade):

        self.has_glasses = True
        self.class_year = class_year
        self.age = age
        self.name = name
        self.class_grade = class_grade

    def speak(self):
        print(self.name, 'is speaking')

    def listening(self):
        print(self.name, 'is listening')

    # function overloading
    def __str__(self):
        return 'has_glasses: {}\n' \
               'class_year: {}\n' \
               'age: {},\n' \
               'name: {}\n' \
               'class_grade: {}\n'.format(self.has_glasses,
                                          self.class_year,
                                          self.age,
                                          self.name,
                                          self.class_grade)


def main():
    ernesto = Student('ernesto', 12, 8, 3.5)
    ernesto.speak()

    dewe = Student('Dewe', 23, 4, 3.65)
    dewe.speak()

    print(dewe)
    dewe.age = 24
    print()
    print(dewe)



main()