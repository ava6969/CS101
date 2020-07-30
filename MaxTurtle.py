import random
import turtle


file = open('colors.txt', 'r')
colors = {}
for line in file.readlines():
    line = line.strip() # stripping
    line_list = line.split() # splitting
    color_name = line_list[0]
    color_code = line_list[2]

    # rgb(255,160,122) - slicing ['r, 'g', 'b' ....]
    color_code = color_code[4:-1] # 255,160,122
    r, g, b = color_code.split(',')  # [255,160,122]
    colors[color_name] = (int(r), int(g), int(b))
file.close()


canvas = turtle.Screen()
canvas.bgcolor('black')
pen = turtle.Turtle()

pen.speed(50)
pen.color('red')
length = 300

for i in range(36000):
    # for _ in range(4):
    pen.circle(length)
        # pen.left(90)
    pen.right(10)
    if i % 36 == 0:
        length -= 10
        color_list = list(colors.keys())
        color = random.choice(color_list)
        pen.pencolor(color)



turtle.done()