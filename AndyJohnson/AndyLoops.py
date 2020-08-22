# i = 0
# while i < 5:
#     print(i)
#     i += 1

# for i in range(0, 5, 1):
#     print(i)


def buy_game(game_price, game_name):
    andy_money = int(input('how much money do you have: '))
    diff = 0
    while andy_money < game_price:
        print('you dont have enough money, try again')
        andy_money = int(input('how much money do you have now: '))
    # TODO if i buy mario, print 'bought mario'
    print('bought', game_name)
    diff = andy_money - game_price
    return diff


def countdown(start):
    if start < 0:
        return None
    else:
        print(start)
        start -= 1
        return countdown(start)


def main():

    # print('welcome to gamestop')
    # choice = int(input('choose game to buy:\n'
    #                    '1) mario $20\n'
    #                    '2) GOW $25\n'
    #                    '>> '))
    #
    # if choice == 1:
    #     price = 20
    # else:
    #     price = 25
    #
    # diff = buy_game(price)
    # print('your change is', diff)
    countdown(1000)


main()
