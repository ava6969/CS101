import turtle


class Shape:
    def __init__(self, bk_color):
        self.screen = turtle.Screen()
        self.screen.bgcolor(bk_color)
        self.pen = turtle.Turtle()

    def draw(self):
        return NotImplemented


class Circle(Shape):
    def __init__(self, radius, bk_color):
        super().__init__(bk_color)
        self.radius = radius

    def draw(self):
        self.pen.circle(self.radius)
        turtle.done()


class Square(Shape):
    def __init__(self, length, bk_color):
        super().__init__(bk_color)
        self.length = length

    def draw(self):
        for _ in range(4):
            self.pen.forward(self.length)
            self.pen.left(90)
        turtle.done()


class Rectangle(Shape):
    def __init__(self, length, bk_color):
        super().__init__(bk_color)
        self.length = length

    def draw(self):
        for _ in range(4):
            self.pen.forward(self.length)
            self.pen.left(90)
        turtle.done()


def main():
    shape = Square(100, 'red')
    shape.draw()

main()