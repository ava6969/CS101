# list
import turtle

cart = ['pen', 'choc', 'cereal']
print('before appending:', cart)

cart.append('flowers')
print('after appending:', cart)

cart[1] = 'veggies'
print('after changing choc:', cart)

cart.insert(1, 'books')
print('after inserting books:', cart)

cart.remove('cereal')
print('after removing cereal:', cart)

# TUPLE
student1 = ('adesola', 'adedewe', 'male', '1234')
student2 = ('victor', 'adedewe', 'male', '12345')
print(student1)

# set
numbers = {1, 2, 4, 5, 1, 1, 2}  # set will only hold unique values
print(numbers)

# dict
# word - > definition
# key -> value

# list example
# student_info = [student1, student2]
#
# for student in student_info:
#     if student[3] == '12345':
#         print(student)

# dict
students_info = {'12345': student1, '1234': student2}

print(students_info['1234'])

canvas = turtle.Screen()
pen = turtle.Turtle()


def square():
    for _ in range(4):
        pen.forward(100)
        pen.left(90)


turtle_commands = {'SQUARE': square,
                   'CIRCLE': pen.circle}
#
# turtle_commands['CIRCLE'](50)

KEYS = turtle_commands.keys()
print(list(KEYS))