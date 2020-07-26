
import turtle

window = turtle.Screen()
# window.bgcolor('black')

pen = turtle.Turtle()

pen.color('red')
pen.begin_fill()
for i in range(4):
    pen.forward(100)
    pen.left(90)
pen.end_fill()

pen.color('white')
pen.begin_fill()
pen.forward(50)
pen.circle(50)
pen.end_fill()



turtle.done()
