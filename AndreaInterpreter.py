import turtle


class TurtleInterpreter:

    def __init__(self, script_name):

        self.instructions = []
        self.process_script(script_name)
        self.screen = turtle.Screen()
        self.pen = turtle.Turtle()

        self.functions = {'F': self.pen.forward,
                          'L': self.pen.left,
                          'R': self.pen.right,
                          'C': self.pen.circle,
                          'PC': self.pen.pencolor}

        self.colors = ['red', 'blue', 'green', 'yellow', 'purple', 'pink']

        self.run()


    def process_script(self, script_name):
        file = open(script_name)

        for line in file.readlines():

            if line[0] == '#' or line[0] == '\n':
                continue

            elif line[0] == '(':
                line = line[1:]
                instr, multiple = line.split(')x')
                commands = []
                for _ in range(int(multiple)):
                    commands.extend(instr.split(', '))

            else:
                line = line.strip()
                commands = line.split(', ')

            self.instructions.append(commands)

    def run(self):

        for instr in self.instructions:
            for command in instr:
                funct, arg = command.split('_')
                if funct == 'PC':
                    self.functions[funct](self.colors[int(arg)])
                else:
                    self.functions[funct](int(arg))
        turtle.done()


def test():
    TurtleInterpreter('script.txt')


if __name__ == '__main__':
    test()




