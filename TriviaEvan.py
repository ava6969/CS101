import random


def preprocess(filename):

    file = open(filename)
    questions = {}

    for line in file.readlines():
        line = line.strip()
        arr = line.split(':')
        question = arr[0]
        answer_points = arr[1].split(',')
        answer = answer_points[0]
        point = answer_points[1]

        questions[question] = (answer, point)

    file.close()

    return questions


def trivia_game(max_point, name, question_dict:dict):
    points = 0
    print('Welcome to my trivia', name,
          '\nYou need',max_point,'points To win the game',
          '\nGoodluck!!!')

    questions = list(question_dict.keys())
    while points < max_point:
        ques = random.choice(questions)
        answer = input(ques)
        true_answer = question_dict[ques][0]
        if answer.lower() == true_answer:
            points += int(question_dict[ques][1])

        else:
            print('Correct Answer: ', question_dict[ques][0], 'not', answer)
            print('GAMEOVER: Total point of ', points)
        print('Total score', points)


def main():

    name = input('Enter Name: ')
    questions = preprocess('questions.txt')
    trivia_game(10, name, questions)

main()