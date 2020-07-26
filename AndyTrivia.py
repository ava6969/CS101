# TODO Create a Preprocess function - converts file to dictionary
# TODO use dictionary to store questions, answers and points

from AndyTriviaOOP import Trivia
# file = open('questions.txt', 'r')
#
# lines = file.readlines()
# stripped_lines = []
#
# for line in lines:
#     line = line.strip()
#     stripped_lines.append(line)
#
# print(stripped_lines)
# file.close()
#
# file = open('new_questions.txt', 'w')
#
# for line in stripped_lines:
#     file.write(line + '\n')
#
# file.close()
import random


def preprocess(filename):
    questions ={}
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


def save(name, score):
    file = open(name+'.txt', 'w')
    file.write(str(score))
    file.close()


def load(name):
    file = open(name+'.txt')
    score = float(file.readline())
    return score


def run_game(max_score, questions_dict, name):

    points = 0
    while points <= max_score:
        questions = list(questions_dict.keys())
        question = random.choice(questions)

        answer = input(question+'\n>> ')
        true_answer, point = questions_dict[question]
        if answer.lower() == true_answer.lower():
            print('Correct: Total Points:', points)
            points += point

            save_ = input('save? Y/N >> ')
            if save_.lower() == 'y':
                save(name, points)

        else:
            print('Game Over!!! Total Points', points)
            break


def main():
    name = input('Enter player name: ')
    trivia = Trivia('questions.txt', name, 20)
    trivia.run_game()


if __name__ == '__main__':
    main()