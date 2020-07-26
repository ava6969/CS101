import random


def convert_file_to_dictionary(trivia_file):
    trivia_data = {}
    # copy to dictionary
    for line in trivia_file.readlines():
        line = line.strip()
        line_list = line.split(',')
        question = line_list[0]
        answer = line_list[1].strip(' ')
        point = line_list[2].strip(' ')
        trivia_data[question] = (answer, point) # adding to the dictionary
    trivia_file.close()

    return trivia_data


def resume_game(name):
    score = 0
    try:
        saved_file = open(name+'.txt')
        score_list = saved_file.readlines()
        score = float(score_list[0])
        print('Successfully resumed from previous game: Total Points',score)
        saved_file.close()
    except:
        score = 0
        print(' ')
    return score


def trivia_game(trivia_data, max_score):
    passed = True
    name = input('what is your name')
    score = resume_game(name)
    save_file = open(name + '.txt', 'w')

    while score < max_score and passed:

        # randomly select a number
        question_list = list(trivia_data.keys())
        question = random.choice(question_list)

        answer = input(question)
        true_answer, point = trivia_data[question]

        if answer.lower() == true_answer:
            score += int(point)
            print('total scores: ', score)
            save = input('type 1 to save:')
            if int(save) == 1:
                save_file.writelines(str(score))
                print('saved gamed with total points', score)
                break

        else:
            passed = False
            print('GameOver: Total Points:', score,
                  'Right Answer:', true_answer)

    save_file.close()


def main():
    trivia_file = open('../../questions.txt', 'r')
    trivia_data = convert_file_to_dictionary(trivia_file)
    max_score = 100
    trivia_game(trivia_data, max_score)


if __name__ == '__main__':
    main()





