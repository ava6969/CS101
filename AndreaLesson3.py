# file processing
# 3 ways - read, write,  append

import random
import AndreaLesson4


def preprocess(filename, debug=False):
    file = open(filename, 'r')

    questions_dict = {}
    for line in file.readlines():
        # string function 1 - strip()
        stripped_line = line.strip()
        # str function 2 - split()
        splitted_line = stripped_line.split(',')
        quest , ans, points = splitted_line
        questions_dict[quest] = ans.strip(' '), int(points)
    file.close()

    if debug:
        for i, (key, value) in enumerate(questions_dict.items(), start=1):
            print('question {}: {} -> {}, {}'.format(i, key, *value))
    return questions_dict


def run(max_point, question_dict):
    score = 0

    questions = list(question_dict.keys())
    while score <= max_point:

        question = random.choice(questions)
        answer = input(question+' ? ')
        true_answer, point = question_dict[question]

        if answer.lower() == true_answer:
            score += point
            print('correct: you have {} total points'.format(score))
        else:
            print("GAMEOVER!! - Total points - ", score)
            break


def main():
    # question_dict = preprocess('questions.txt')
    # run(10, question_dict)
    player_name = input('Player name > ')
    game = AndreaLesson4.Trivia(player_name, 'questions.txt', 10)
    game.run()



main()
