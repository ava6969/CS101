# for loops and data structures

# tony_is_running = True
#
# while tony_is_running:
#     answer = input('is tony still running Y/N?')
#     if answer == 'N':
#         print('Tony stopped running')
#         break
#     print('Tony is running')
#

# counter = 5
# while counter >= 1:
#     print('Tony is running', counter, 'seconds left')
#     counter -= 1
# print('Tony stopped running')
#
# for counter in range(5, 0, -1):
#     print('Tony is running', counter, 'seconds')
# print('Tony stopped running')


# data structures
# list_of_things = ['lesson this morning',
#                   'did homework',
#                   'read books',
#                   'late night classes',
#                   'run this afternoon']

print('How to make a cereal? ')
ingredients = []

for i in range(5):
    ing = input('ingredient ' + str(i) + ' > ')
    ingredients.append(ing)

print(ingredients)
