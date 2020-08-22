import turtle

canvas = turtle.Screen()
pen = turtle.Turtle()

# basic commands
def polygon(side, size):
    for _ in range(side):
        pen.forward(size)
        pen.left(float(360/side))

pen.color('red')

pen.begin_fill()
polygon(7, 100)

pen.end_fill()

turtle.done()


