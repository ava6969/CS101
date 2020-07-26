tries = 5
max_point = 100
points = 0

# random questions

while points < max_point:

    number = int(input('Enter a Number between 1 - 10: '))

    if number == 1:
        answer = input('7 * 8 = ')
        if answer == '56':
            points += 1
        else:
            print('GameOver: Total Points =', points)
            break
    elif number == 2:
        answer = input('What is the color of a banana? ')
        if answer.lower() == 'yellow':
            points += 5
        else:
            print('GameOver: Total Points =', points)
            break
    elif number == 3:
        answer = input('15 + 47 = ')
        if answer.lower() == '62':
            points += 1
        else:
            print('GameOver: Total Points =', points)
            break
    elif number == 4:
        answer = input('Who is the current US President? ')
        if answer.lower() == 'trump':
            points += 5
        else:
            print('GameOver: Total Points =', points)
            break
    elif number == 5:
        answer = input('How many states are there in the US? ')
        if answer.lower() == '50':
            points += 50
        else:
            print('GameOver: Total Points =', points)
            break
    elif number == 6:
        answer = input('12 * 13 = ')
        if answer.lower() == '156':
            points += 1
        else:
            print('GameOver: Total Points =', points)
            break
    elif number == 7:
        answer = input('Who is the richest man in the world? ')
        if answer.lower() == 'jeff':
            points += 20
        else:
            print('GameOver: Total Points =', points)
            break
    elif number == 8:
        answer = input('2 + 3 = ')
        if answer.lower() == '5':
            points += 1
        else:
            print('GameOver: Total Points =', points)
            break
    elif number == 9:
        answer = input('5 * 8 = ')
        if answer.lower() == '40':
            points += 5
        else:
            print('GameOver: Total Points =', points)
            break
    else:
        answer = input('How many seasons are there? ')
        if answer.lower() == '4':
            points += 5
        else:
            print('GameOver: Total Points =', points)
            break

    print('Total Score:',points)