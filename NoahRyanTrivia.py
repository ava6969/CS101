import random


def convert_file_to_dict(file_name):
    question_dict = {}

    question_file = open(file_name)

    for line in question_file.readlines():
        line = line.strip()
        line_list = line.split(',')
        question = line_list[0]
        answer = line_list[1].strip(' ')
        score = int(line_list[2])
        question_dict[question] = (answer, score)

    question_file.close()
    return question_dict


question_dict = convert_file_to_dict('questions.txt')
max_point = 100
points = 0
passed = True

# random questions
while points < max_point and passed:
    question_list = list(question_dict.keys())
    question =  random.choice(question_list)
    answer = input(question)

    (true_answer, question_point) = question_dict[question]
    if answer.lower() == true_answer:
        points += question_point
        print('Total Score =', points)
    else:
        passed = False
        print('You lost: Total score:', points)

if passed:
    print('Congratulation You Won')
