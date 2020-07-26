

def _sum(_list):

    res = 0
    for number in _list:
        res += number
    return res

print(_sum([3, 4, 6, 76]))

# cart = []
#
# for _ in range(5):
#     item = input('what do you want to buy? ')
#     cart.append(item)
#
# print(cart[3])
# print(cart)
# cart[2] = 2
# print(cart)
#
# for item in cart:
#     if item == 'meal':
#         print('we have a meal in the cart')

# tuple
pos = (0.1, -.3, 1)
print(pos)
pos = (0.1, 1, 2)
print(pos[2])

# dictionary
student_info = {'andy': ('andy johnson', 12),
                'adesola': ('adesola adedewe ', 23),
                'andy1': 23}
print(student_info['andy'])

# set - has all unique values

lotto = {2, 4, 3, 3,6}
print(lotto)