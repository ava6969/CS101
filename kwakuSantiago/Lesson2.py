
# if statements

amount_left = int(input('How much do you have in your wallet? '))

game_choice = int(input('choose your game:\n1) COD\n2) FIFA\n3) MINECRAFT\n>> '))


# game prices
call_of_duty_price = 65
fifa_price = 50
minecraft_price = 20


# and/or

if amount_left >= call_of_duty_price and game_choice == 1:
    print('bought COD')
    amount_left = amount_left - call_of_duty_price
if amount_left >= fifa_price:
    print('bought FIFA')
    amount_left -= fifa_price
if amount_left >= minecraft_price:
    print('bought minecraft')
    amount_left -= minecraft_price
if amount_left >= call_of_duty_price and game_choice == 1:
    print('bought COD')
    amount_left = amount_left - call_of_duty_price
if amount_left >= minecraft_price:
    print('bought minecraft')
    amount_left -= minecraft_price
else:
    print('You dont have enough money')
