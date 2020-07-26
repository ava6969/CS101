# 4 major data types
# int, float, boolean, strings

# Examples
#1 variables

# age = 12
# money = 12
#
# print(age)
#
# grade = 78.2
# _money = 100.25
#
# print(grade)
# is_dancing = False
# is_talking = True
#
# print(is_dancing)
#
# first_name = 'Tony'
# last_name = 'Li'
# print(first_name, last_name)

# + - / * %

# x = 2
# y = 3
# z = x + y
# heading = 'z ='
# print(heading, z)

# conditionals

money = int(input('How much do you have?' ))
game_price = 50
demo_price = game_price/2

if money >= game_price:
    print('bought full game')
    remainder = money - game_price
    print('change ', remainder)
elif money >= demo_price:
    print('bought game demo')
else:
    print('get more money and come back')
    print('you need to pay', game_price-money)