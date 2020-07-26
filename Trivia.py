import random


class Trivia:
    def __init__(self, player_name, filename, max_point):
        self.question_dict = {}
        self.convert_file_to_dict(filename)
        self.max_point = max_point
        self.p_name = player_name
        self.points = 0
        self.has_lost = False
        self.question = ''

    def convert_file_to_dict(self, file_name):
        question_file = open(file_name)

        for line in question_file.readlines():
            line = line.strip()
            line_list = line.split(',')
            question = line_list[0]
            answer = line_list[1].strip(' ')
            score = int(line_list[2])
            self.question_dict[question] = (answer, score)
        question_file.close()

    def generate_question(self):
        question_list = list(self.question_dict.keys())
        self.question = random.choice(question_list)

    def validate_answer(self, answer):
        (true_answer, question_point) = self.question_dict[self.question]
        correct = answer.lower() == true_answer
        if not correct:
            question_point = 0
        return correct, question_point

    def run_game(self):
        # random questions
        while self.points < self.max_point and not self.has_lost:
            self.generate_question()
            answer = input(self.question)

            correct, question_point = self.validate_answer(answer)

            if correct:
                self.points += question_point
                print('Total Score =', self.points)
            else:
                self.has_lost = True
                print('You lost: Total score:', self.points)

        if not self.has_lost:
            print('Congratulation {} Won'.format(self.p_name))


def main():
    game = Trivia('dewe', 'questions.txt', 10)
    game.run_game()


if __name__ == '__main__':
    main()