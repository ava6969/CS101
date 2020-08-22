import random


class Trivia:

    def __init__(self, file_name, _name, max_score):

        self.questions_dict = self.preprocess(file_name)
        self.points = 0
        self.max_score = max_score
        self.name = _name

    def preprocess(self, filename):
        questions = {}
        file = open(filename)

        for line in file.readlines():
            line = line.strip()
            splitted_line = line.split(',')
            question = splitted_line[0]
            answer = splitted_line[1].strip(' ')
            point = float(splitted_line[2])

            questions[question] = (answer, point)

        file.close()
        return questions

    def save(self, score):
        file = open(self.name + '.txt', 'w')
        file.write(str(score))
        file.close()

    def load(self, name):
        try:
            file = open(name + '.txt')
            score = float(file.readline())
            print('Load Successful: Initial Score', score)

        except:
            score = 0

        return score

    def run_game(self):

        self.points = self.load(self.name)

        while self.points <= self.max_score:
            questions = list(self.questions_dict.keys())
            question = random.choice(questions)

            answer = input(question + '\n>> ')
            true_answer, point = self.questions_dict[question]
            if answer.lower() == true_answer.lower():
                print('Correct: Total Points:', self.points)
                self.points += point

                save_ = input('save? Y/N >> ')
                if save_.lower() == 'y':
                    self.save( self.points)

            else:
                print('Game Over!!! Total Points', self.points)
                break