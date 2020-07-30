def print_list(cart):
    for i, item in enumerate(cart):
        print('index {}: {}'.format(i, item))


def _min(x, y):
    return x if x < y else y


def list_info(_list):

    return min(_list), sum(_list), max(_list), len(_list)

# while loops

# i = 0
# while i != 11:
#     print(i)
#     i += 1
#
# name = 'andrea'
# while i < 10 and name == 'andrea' :
#     print(i)
#     i += 1
#
# for i in range(1, 10 + 1, 2):
#     print(i)
#
# print()
#
# for i in range(10 + 1):
#     print(i)

# data structures
# list
cart = ['choc', 'cereal', 67]
cart[0] = 'd'
# iterate

# for i in range(len(cart)):
#     item = cart[i]
#     print('index {}: {}'.format(i, item))
#
# print()
#
# for item in cart:
#     print(item)
#
# print()
#
# for i, item in enumerate(cart):
#     print('index {}: {}'.format(i, item))

# operations on list
#
# for _ in range(5):
#     item = input('hey!! what do you want? ')
#     cart.append(item)
#
# for i, item in enumerate(cart):
#     print('index {}: {}'.format(i, item))
#
# cart.insert(2, 'meat')
#
# for i, item in enumerate(cart):
#     print('index {}: {}'.format(i, item))

# tuple

# info = ('andrea', 'hosier', 12)
# info_list = list(info)
# print(info_list[0])
#
# # set
#
# survey = ['tom', 'dave', 'dewe', 'andrea', 'tom', 'dave']
#
#
# _survey_names = set(survey)
# print_list(_survey_names)
#
# # dictionary
# oxford_dict = { 'take': 'to take',
#                 'eat': 'to eat'}
#
# print(oxford_dict['eat'])

numbers = [4, 12, 4, -1]
_mini, _sum, _max, _count = list_info(numbers)
print(_mini)