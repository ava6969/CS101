# name = 'sid'
# age = 12
# # print('my name is', name, 'i am ', age, 'years old ')
# print('my name is {}, I am {} years old'.format(name, age))

import turtle


shape = input('Select a shape:\n'
              '1) Square\n'
              '2) Triangle\n'
              '3) Circle\n'
              '4) Rectangle\n'
              '>> ')

if int(shape) == 1:
    length = int(input('length of sqaure? '))
    # draw square
    canvas = turtle.Screen()
    # canvas.bgcolor('white')
    pen = turtle.Turtle()
    pen.color('green')
    pen.begin_fill()
    for i in range(4):
        pen.forward(length)
        pen.left(90)
    pen.end_fill()

elif int(shape) == 2:
    length = int(input('length of triangle? '))
    angle = int(input('angle of triangle? '))
    canvas = turtle.Screen()
    # canvas.bgcolor('white')
    pen = turtle.Turtle()
    for i in range(3):
        pen.forward(length)
        pen.left(180 - angle)


elif int(shape) == 3:
    radius = int(input('radius of circle? '))
    # draw circle
    canvas = turtle.Screen()
    # canvas.bgcolor('white')
    pen = turtle.Turtle()
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

else:
    length = int(input('length of rectangle? '))
    width = int(input('width of rectangle? '))
    canvas = turtle.Screen()
    # canvas.bgcolor('white')
    pen = turtle.Turtle()
    pen.color('green')
    pen.begin_fill()
    for i in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(length)
        pen.left(90)

    pen.end_fill()

turtle.done()