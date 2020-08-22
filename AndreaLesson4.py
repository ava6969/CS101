import random
import time

class Trivia:

    # constructor
    def __init__(self, player_name, file_name, maxpoint, debug_mode=False):
        self.dict_ = {}
        self.player_name = player_name
        self.debug_mode = debug_mode
        self.preprocess(file_name)
        self.max_point = maxpoint
        self.score = 0
        random.seed(time.time())


    def preprocess(self, filename):
        file = open(filename, 'r')

        for line in file.readlines():
            # string function 1 - strip()
            stripped_line = line.strip()
            # str function 2 - split()
            splitted_line = stripped_line.split(',')
            quest , ans, points = splitted_line
            self.dict_[quest] = ans.strip(' '), int(points)
        file.close()

        if self.debug_mode:
            for i, (key, value) in enumerate(self.dict_.items(), start=1):
                print('question {}: {} -> {}, {}'.format(i, key, *value))

    def save(self):
        save_file = open(self.player_name, 'w')
        save_file.write(str(self.score))
        save_file.close()

    def load(self):
        try:
            save_file = open(self.player_name, 'r')
            self.score = int(save_file.readline())
            save_file.close()
        except:
            self.score = 0


    def run(self):
        self.load()
        questions = list(self.dict_.keys())
        while self.score <= self.max_point:

            question = random.choice(questions)
            answer = input(question+' ? ')
            true_answer, point = self.dict_[question]

            if answer.lower() == true_answer:
                self.score += point
                print('correct: you have {} total points'.format(self.score ))
                self.save()
            else:
                print("GAMEOVER!! - Total points - ", self.score )
                break