import turtle
import random

class ShapeDrawer:

    def __init__(self, board_color='white', pen=None):
        board = turtle.Screen()
        board.bgcolor(board_color)
        if pen == None:
            self.pen = turtle.Turtle()
        else:
            self.pen = pen

    def square_circle(self, l, radius, angle, square_color, circle_color):
        for _ in range(4):
            self.pen.color(square_color)
            self.pen.begin_fill()
            self.draw_square( l)
            self.pen.end_fill()

            self.pen.penup()
            self.pen.forward(l // 2)
            self.pen.pendown()

            self.pen.color(circle_color)
            self.pen.begin_fill()
            self.draw_circle( radius)
            self.pen.end_fill()

            self.pen.penup()
            self.pen.back(l // 2)
            self.pen.pendown()
            self.pen.left(angle)

    def draw_circle(self, radius):
        self.pen.circle(radius)

    def draw_square(self, length):
        for _ in range(4):
            self.pen.forward(length)
            self.pen.left(90)

