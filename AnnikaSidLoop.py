import random
# while

# i = 0
# while i <= 5:
#     print(i)
#     i = i + 1

# for i in range(0, 10, 3):
#     print(i)

# for loop


# Data Structures
# list
import turtle

colors = ['red', 'blue', 'green']


print(colors)
colors.append('white')
print(colors)
for i in range(len(colors)):
    print('index {}: {}'.format(i, colors[i]))

print()
for color in colors:
    print(color)

print()
for i, color in enumerate(colors):
    print('index {}: {}'.format(i, color))

random_color = random.choice(colors)
print('randomly generated color is ', random_color)

# slicing
new_colors = colors[2:]
print(new_colors)


screen = turtle.Screen()
pen = turtle.Turtle()
screen.bgcolor('black')
pen.speed(15)
pen.goto(0, -500)
radius = 700

i = 0
while True:
    if i % 2 == 0:
        color = 'black'
    else:
        color = 'white'
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()
    radius -= 10
    if radius == 0:
        radius = 200
    i += 1


turtle.done()


