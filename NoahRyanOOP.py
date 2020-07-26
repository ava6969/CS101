# OBJECT ORIENTED PROGRAMMING

# ATTRIBUTES (data type)
# - num of EYES - int, num of NOSE - int , NAME - str, AGE - int,
# STUDENT - true/false, SCHOOL_GRADE - float, PERSONALITY - string
# SCHOOL_GRADES -list/ dict

# BEHAVIORS
# - WALK(), TALK(), WRITE()
import turtle

import NoahRyanTurtle
import NoahRyanFunctions

class Student:
    def __init__(self, name, age, is_student, pers):
        self.num_of_eyes = 2
        self.num_of_nose = 1
        self.name = name
        self.age = age
        self.is_student = is_student
        self.grade = 2.5
        self.personality = pers
        self.grades = []

    def walk(self):
        print(self.name, 'is walking')

    def talk(self):
        print(self.name, 'is talking')

    def write(self):
        print(self.name, 'is writing')


def main():
    noah = Student('noah', 12, True, 'fun')
    noah.walk()

    ryan = Student('ryan', 12, True, 'exciting')
    ryan.talk()

    board = turtle.Screen()
    board.bgcolor('white')
    pen = turtle.Turtle()
    pen.speed(20)
    NoahRyanTurtle.draw_square(pen, 100)
    turtle.done()

main()

