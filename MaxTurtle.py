import random
import turtle

canvas = turtle.Screen()
canvas.bgcolor('black')
pen = turtle.Turtle()

pen.speed(50)
pen.color('red')
colors = ['green', 'red', 'white', 'orange', 'purple', 'pink', 'yellow', 'blue']
length = 300

for i in range(36000):
    # for _ in range(4):
    pen.circle(length)
        # pen.left(90)
    pen.right(10)
    if i % 36 == 0:
        length -= 10
        pen.color(random.choice(colors))



turtle.done()