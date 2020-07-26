import turtle
my_window = turtle.Screen()
my_window.bgcolor("white")       # creates a graphics window

my_pen = turtle.Turtle()
length = 150
for i in range(4):
    my_pen.forward(length)
    my_pen.right(90)

my_pen.penup()
my_pen.forward(length//2)
my_pen.right(90)
my_pen.forward(length)
my_pen.left(90)
my_pen.pendown()
my_pen.circle(length//2)

my_pen.penup()
my_pen.forward(length//2)
my_pen.left(90 + 30)
my_pen.pendown()
my_pen.forward(length)
my_pen.left(120)
my_pen.forward(length)

turtle.done()