import random
import turtle

import Trivia
import ShapeDrawer

def main():
    # game = Trivia.Trivia('Dewe', 'questions.txt', 20)
    # game.run_game()

    shapeDrawer = ShapeDrawer.ShapeDrawer('green')
    l = 100
    angle = 90

    colors = ['red', 'blue', 'green', 'orange', 'black']

    for _ in range(4):
        square_color = random.choice(colors)
        circle_color = random.choice(colors)
        shapeDrawer.square_circle( l, l // 2, angle, square_color, circle_color)
        shapeDrawer.pen.forward(l * 2)
        shapeDrawer.pen.left(angle)

    turtle.done()


if __name__ == '__main__':
    main()