# print('Welcome to the Escape Room')
# name = input('Enter Your name >> ')
# age = input('Enter Your age >> ')

# print(int(False))

# if int(age) >= 18:
#     new_name = name + ' is an adult'
#     print(new_name)
# else:
#     print(name + ' is not an adult')

# ask for name = Noah
# ask for age = 18

# check if age is less than 18
    # if age is less than 18
        # Noah is an adult
    # else
        # Noah is not an adult


# while int(age) < 18:
#     print(name, 'is not an adult')
#     age = input('Enter Your age >> ')

# HINT if x == 1 and y > 4:
tries = 5

while tries > 0:
    score = input('What is 2 + 2? ')
    if int(score) == 4:
        print('Well Done!!')
        break

    tries -= 1 # tries = tries - 1
    print('you have ', tries, 'more tries')
