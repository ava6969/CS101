# i = 10
# statement that starts the loop
# terminator

passed = True
points = 0
while passed:
    key = int(input('Enter a number between 1-5 >> '))
    if key == 1:
        answer = input('what is 2 + 2?')
        if int(answer) == 4:
            points += 4
        else:
            print('GameOver : Total Score is', points)
            passed = False

    elif key == 2:
        answer = input('what is 10 + 2?')
        if int(answer) == 12:
            points += 12
        else:
            print('GameOver : Total Score is', points)
            passed = False

    elif key == 3:
        answer = input('what is 3 * 2?')
        if int(answer) == 6:
            points += 6
        else:
            print('GameOver : Total Score is', points)
            passed = False

    elif key == 4:
        answer = input('what is 4 / 2?')
        if int(answer) == 2:
            points += 2
        else:
            print('GameOver : Total Score is', points)
            passed = False
    else:
        answer = input('what is 2 * 2 * 2?')
        if int(answer) == 8:
            points += 8
        else:
            print('GameOver : Total Score is', points)
            passed = False

    print('Current Score is', points)
