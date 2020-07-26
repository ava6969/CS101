import turtle
import random


def square_circle(pen, l, radius, angle, square_color, circle_color):
    for _ in range(4):
        pen.color(square_color)
        pen.begin_fill()
        draw_square(pen, l)
        pen.end_fill()

        pen.penup()
        pen.forward(l//2)
        pen.pendown()

        pen.color(circle_color)
        pen.begin_fill()
        draw_circle(pen, radius)
        pen.end_fill()

        pen.penup()
        pen.back(l//2)
        pen.pendown()
        pen.left(angle)


def draw_circle(pen, radius):
    pen.circle(radius)


def draw_square(pen, length):
    for _ in range(4):
        pen.forward(length)
        pen.left(90)


def main():
    board = turtle.Screen()
    board.bgcolor('white')
    pen = turtle.Turtle()
    pen.speed(20)
    l = 100
    angle = 90

    colors = ['red', 'blue', 'green', 'orange', 'black']

    for _ in range(4):
        square_color = random.choice(colors)
        circle_color = random.choice(colors)
        square_circle(pen, l, l//2, angle, square_color, circle_color)
        pen.forward(l*2)
        pen.left(angle)

    turtle.done()

if __name__ == '__main__':
    main()