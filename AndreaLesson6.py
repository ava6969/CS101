#
# with open('pract.txt') as file:
#     temp_list = []
#
#     # split and copy to list
#     temp_list2 = [line2.strip().split(': ') for line2 in file.readlines()]
#
#     for line in file.readlines():
#         strippedline = line.strip()
#         splittedline = strippedline.split(': ')
#         temp_list.append(splittedline)
#
#     print(temp_list)
#     print(temp_list2)
#
#     print(len(temp_list2) == len(temp_list))
#
#
# contact_list = set()
# list_ = []
# longest_length = 0

#
# for line in file.readlines():
#     strippedline = line.strip()
#
#     splittedline = strippedline.split(': ')
#     name, message = splittedline
#     contact_list.add(name)
#     list_.append((name, message))
#
#     if len(message.split(' ')) > longest_length:
#         longest_length = len(message.split(' '))
#
# print(list_)
# print(contact_list)
# print(longest_length)

import turtle


# Abstract Class
class Shape:
    canvas = turtle.Screen()
    pen = turtle.Turtle()

    def __init__(self, length):
        self.length = length

    def draw(self):
        return NotImplemented


class Rectangle(Shape):
    def __init__(self, length, width):
        super(Rectangle, self).__init__(length)
        self.width = width

    def draw(self):
        for _ in range(2):
            self.pen.forward(self.length)
            self.pen.left(90)
            self.pen.forward(self.width)
            self.pen.left(90)


class Circle(Shape):
    def __init__(self, radius):
        super(Circle, self).__init__(radius)

    def draw(self):
        self.pen.circle(self.length)


rect = Rectangle(100, 20)
rect.draw()

circle = Circle(50)
circle.draw()

turtle.done()