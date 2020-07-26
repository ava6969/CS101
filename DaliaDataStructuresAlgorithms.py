
# list
# cart = []
#
# cart.append('banana')
# cart.append('bread')
# cart.append('choc')
# cart.append(2)
# cart.extend(['choc', 'dalia', 'dewe', 2, 2])
#
# n_list = len(cart)
# print(n_list)
#
# for i in range(n_list):
#     item = cart[i]
#     if i == 1:
#         cart[i] = 'i = 1'
#     print(item)
#
# for item in cart:
#     print(item)
#
# for i, item in enumerate(cart):
#     print(i, item)
#
# print(cart)
#
# # list operations
# def search(n_list, value):
#     for item in n_list:
#         if item == value:
#             return True
#
#     return False
#
#
# def count(n_list, value):
#     _count = 0
#
#     for item in n_list:
#
#         if item == value:
#             _count += 1
#
#     return _count
#
#
#
# value = 'banana'
#
# found = search(cart, value)
#
# n = count(cart, 2)
# print(n)
# # print(count(cart, 'choc'))
#
# if found:
#     print(value, 'is found')
# else:
#     print(value, 'is not found')
#

# set

_set = {2, 2, 3, 4, 4, 5, 5}
print(_set)

_list = list(_set)
print(_list[2])

# tuple
info = ('dewe', 25, '22.7')
print(info[1])

# dictionary
_dict = {('name', 2):'adesola',
         'second name': 'adedewe',
         'age': 23}

print(_dict[('name', 2)])