import pygame as pg
import sys, time, random, math
from pygame.locals import *


class Pong:
    def __init__(self, screen_dim, ball_color):
        pg.init()
        self.screen_dim = screen_dim
        self.display = pg.display.set_mode((screen_dim[0], screen_dim[1]), 0, 32)
        self.color = {'white': (255, 255, 255),
                      'blue': (0, 0, 255),
                      'red': (255, 0, 0),
                      'green': (0, 255, 0),
                      'black': (0, 0, 0)}
        self.display.fill(self.color['white'])

        self.player1_loc = (800, 100)
        self.player2_loc = (100, 50)
        self.ball_loc = (500, 500)
        self.paddle_dim = (25, 100)

        self.ball_speed = 2
        self.ball_radius = 20
        self.ball_dir = (0, 0)
        self.ball_color = ball_color

        self.game_stat = {'player1 score': 0,
                          'player1_color': self.color['blue'],
                          'player2_color': self.color['red'],
                          'player2 score': 0}

    def move_ball_randomly(self):
        ball_dir_x = math.sin(3 * math.pi / 2)
        choice = random.randint(0, 1)
        if choice == 0:
            ball_dir_y = math.cos(2 * math.pi / 2)
        elif choice == 1:
            ball_dir_y = math.cos(4 * math.pi / 2)
        self.ball_dir = (ball_dir_x, ball_dir_y)

    def render(self):
        pg.draw.rect(self.display, self.game_stat['player1_color'], (self.player1_loc[0],
                                                                     self.player1_loc[1],
                                                                     self.paddle_dim[0],
                                                                     self.paddle_dim[1]))
        pg.draw.rect(self.display, self.game_stat['player2_color'], (self.player2_loc[0],
                                                                     self.player2_loc[1],
                                                                     self.paddle_dim[0],
                                                                     self.paddle_dim[1]))
        pg.draw.circle(self.display, self.ball_color, (self.ball_dir[0], self.ball_dir[0]), self.ball_radius)

    def edgeX(self, x, width):
        if x >= self.screen_dim[0] - width:
            x = self.screen_dim[0] - width
        if x <= 0:
            x = 0
        return x

    def edgeY(self, y, height):
        if y >= self.screen_dim[1] - height:
            y = self.screen_dim[1] - height
        if y <= 0:
            y = 0
        return y

    def ballEdgeY(self, y, radius):
        if y >= self.screen_dim[1] - radius:
            ballDirectionY = -self.ball_dir[1]
        if y <= 0:
            ballDirectionY = -self.ball_dir[1]
        self.ball_dir = (self.ball_dir[0], ballDirectionY)

    def ballEdge(self, width, height, direction):
        if self.player1_loc[0] <= self.ball_loc[0] <= self.player1_loc[0]  + width and \
                self.player1_loc[1]  <= self.ball_loc[1] <= self.player1_loc[1] + height:
            direction = -math.pi / 2
            return direction

        elif self.player2_loc[0] <= self.ball_loc[0] <= self.player2_loc[0] + width and \
                self.player2_loc[1] <= self.ball_loc[1] <= self.player2_loc[1] + height:
            direction = math.pi / 2
            return direction
        else:
            return direction

    def scoreBlue(self, xBall, screenWidth, blueScore):
        if xBall >= screenWidth:
            blueScore += 1
            return blueScore
        else:
            return blueScore

    def scoreRed(self, xBall, redScore):
        if xBall <= 0:
            redScore += 1
            return redScore
        else:
            return redScore

    def check_input(self):
        currentKey = pg.key.get_pressed()
        self.display.fill(self.color['white'])
        if currentKey[K_UP]: self.player1_loc[1] -= 5
        if currentKey[K_DOWN]: self.player1_loc[1] += 5
        if currentKey[K_LEFT]: self.player1_loc[0] -= 5
        if currentKey[K_RIGHT]: self.player1_loc[0] += 5
        if currentKey[K_w]: y2 -= 5
        if currentKey[K_s]: y2 += 5

    def run(self):

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

            self.display.fill(self.color['white'])
            self.check_input()

            redPaddleX = edgeX(x1, screenWidth, width)
            redPaddleY = edgeY(y1, screenHeight, height)
            bluePaddleX = edgeX(x2, screenWidth, width)
            bluePaddleY = edgeY(y2, screenHeight, height)
            ballDirectionX = ballEdge(xBall, yBall, bluePaddleX, bluePaddleY, redPaddleX, redPaddleY, width, height,
                                      ballDirectionX)
            ballDirectionY = ballEdgeY(yBall, screenHeight, radius, ballDirectionY)
            xBall += speed * ballDirectionX
            yBall -= speed * ballDirectionY
            pg.draw.rect(display, red, (redPaddleX, redPaddleY, width, height))
            pg.draw.rect(display, blue, (bluePaddleX, bluePaddleY, width, height))
            pg.draw.circle(display, black, (xBall, yBall), radius)
            blueScore = scoreBlue(xBall, screenWidth, startingBlueScore)
            blueScore_font = pg.font.Font(None, 50)
            blueScore_surf = blueScore_font.render(str(blueScore), 1, (0, 0, 0))
            blueScore_pos = [10, 10]
            startingBlueScore = blueScore
            display.blit(blueScore_surf, blueScore_pos)
            redScore = scoreRed(xBall, startingRedScore)
            redScore_font = pg.font.Font(None, 50)
            redScore_surf = redScore_font.render(str(redScore), 1, (0, 0, 0))
            redScore_pos = [960, 10]
            display.blit(redScore_surf, redScore_pos)
            startingRedScore = redScore
            pg.display.update()
            if xBall <= 0 or xBall >= screenWidth:
                xBall = 500
                speed = initialSpeed
            speed += 0.01


draw()

'''
Scrap:
direction=math.radians(direction)
        xBall+=speed*math.cos(direction)
        yBall-=speed*math.cos(direction)
'''

'''
Drawing Function:
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        currentKey=pg.key.get_pressed()
        if currentKey[K_UP]:y-=5
        if currentKey[K_DOWN]:y+=5
        if currentKey[K_LEFT]:x-=5
        if currentKey[K_RIGHT]:x+=5
        pg.display.update()
        pg.draw.rect(display,red,(x,y,width,height))
'''

'''
print ("Hello World")
numCookies=5
print ("I have",numCookies,"cookies!")
name="Avery"
print ("My name is",name)
list=["Avery", "Lucas", "Jordan"]
print ("I am here with", list[1],list[2])
for name in list:
    print (name)
isAlive = True
healthpoints = 10
while isAlive == True:
    print ("I have", healthpoints, "healthpoints.")
    healthpoints = healthpoints-1
    if healthpoints<=0:
        print ("I died")
        isAlive=False
def add(x):
    return x+x
print (add(2))
'''
