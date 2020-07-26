import turtle


class Shape:
    board = turtle.Screen()
    pen = turtle.Turtle()

    def __init__(self, length, fill=False, color='black', bg_color='white'):
        # Shape.board.bgcolor(bg_color)
        self.color = color
        self.fill = fill
        self.length = length

    def draw(self):
        return NotImplemented

    def join(self, shape):
        return NotImplemented


class Triangle(Shape):
    def __init__(self, length, angle=60, fill=False, color='black', bg_color='white'):
        super(Triangle, self).__init__(fill, length, color, bg_color)
        self.angle = angle

    def draw(self):
        Shape.pen.color(self.color)
        if self.fill:
            Shape.pen.begin_fill()

        for _ in range(3):
            Shape.pen.forward(self.length)
            Shape.pen.left(180-self.angle)
        if self.fill:
            Shape.pen.end_fill()
        turtle.done()


class Rectangle(Shape):
    def __init__(self, length, width, fill=False, color='black', bg_color='white'):
        super(Rectangle, self).__init__(length, fill, color, bg_color)
        self.width = width

    def draw(self):

        Shape.pen.color(self.color)
        if self.fill:
            Shape.pen.begin_fill()

        for _ in range(2):
            Shape.pen.forward(self.width)
            Shape.pen.left(90)
            Shape.pen.forward(self.length)
            Shape.pen.left(90)
        if self.fill:
            Shape.pen.end_fill()
        turtle.done()


class Square(Shape):
    def __init__(self, length, fill=False, color='black', bg_color='white'):
        super(Square, self).__init__(length, fill, color, bg_color)

    def draw(self):

        Shape.pen.color(self.color)
        if self.fill:
            Shape.pen.begin_fill()

        for _ in range(4):
            Shape.pen.forward(self.length)
            Shape.pen.left(90)
        if self.fill:
            Shape.pen.end_fill()
        turtle.done()


class Polygon(Shape):
    def __init__(self, n_sides, length, fill=False, color='black', bg_color='white'):
        super(Polygon, self).__init__(length, fill, color, bg_color)
        self.n_sides = n_sides

    def draw(self):

        angle = 360 / self.n_sides
        Shape.pen.color(self.color)
        if self.fill:
            Shape.pen.begin_fill()

        for _ in range(self.n_sides):
            Shape.pen.forward(self.length)
            Shape.pen.left(angle)
        if self.fill:
            Shape.pen.end_fill()
        turtle.done()


def main():

    triangle = Polygon(7, 100, fill=True, color='red')
    square = Rectangle(100,20, fill=True, color='blue')
    triangle.draw()
    square.draw()


if __name__ == '__main__':
    main()
