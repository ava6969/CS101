# data types
# int, str, float and bool
import random
import pygame, sys
from pygame.locals import *

age = 20
print(age, 'is of data type',type(age))

weight = 162.2
print(weight, 'is of data type', type(weight))

lucasIsReadingNow = True
#  different operations on bool
age_greater_than_eighteen = age < 18
w_greater_than_age = weight > age or weight > 180
print(w_greater_than_age, 'is of data type', type(w_greater_than_age))

name = 'lucas hood'
print(name, 'is of data type', type(name))

condition = age > 9

while age > 9:
    if age > 18 and name == 'lucas hood':
        print('adult')
    elif age > 13 and weight < 180:
        print('teen')
    else:
        print('kid')

    age -= 1

_max = 20
for i in range(10, _max + 1, 3):
    print(i)

ages = [12, 20, 50 , 100]

for i in range(len(ages)):
    age = ages[i]
    print(i,':',age)

for age in ages:
    print(age)

for i, age in enumerate(ages):
    print(i,':',age)

pygame.init()
WIDTH = 500
HEIGTH = 250
screen = pygame.display.set_mode((WIDTH, HEIGTH))
FPS = 200
clock = pygame.time.Clock()


i = 0
R = 50
# game loop
while True:
    clock.tick(FPS)
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    screen.fill(green)
    pygame.display.update()