import random
import turtle

class AndyTurtleInterpreter:

    def __init__(self, script):
        self.colors = {}
        self.command_list = []
        self.preprocess_colors()
        self.preprocess_script(script)


    def preprocess_colors(self):
        color_file = open('../colors.txt')

        for line in color_file.readlines():
            line_list = line.strip().split()
            color_name, color_code, dec_code = line_list
            dec_code_list = dec_code[4:-1].split(',')
            try:
                r, g, b = dec_code_list
            except:
                pass
            self.colors[color_name] = (color_code, (int(r), int(g), int(b)))

        color_file.close()

    def beautiful_turtle(self):

        canvas = turtle.Screen()
        canvas.bgcolor('black')
        pen = turtle.Turtle()

        pen.speed(20)
        pen.color(random.choice(list(self.colors.keys())))
        length = 300

        for i in range(360):
            # for _ in range(4):
            #     pen.forward(length)
            #     pen.left(90)
            pen.circle(length)
            pen.right(10)
            if i % 36 == 0:
                length -= 10
                pen.color(random.choice(list(self.colors.keys())))

        turtle.done()

    def preprocess_script(self, script):
        file  = open(script)

        for line in file.readlines():
            instruction = []
            if line[0] == '(':
                line_list = line[1:].strip().split(')x')
                command, n_time = line_list

                for _ in range(int(n_time)):
                    instruction.append(command)
            else:
                line_list = line.split(',')
                for command in line_list:
                    instruction.append(command)
        file.close()



def main():

    interpreter = AndyTurtleInterpreter('script.txt')

main()