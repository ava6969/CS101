# # list
# _list1 = ['hi', 'hello', 2]
# _list2 = [4, 5, 10]
#
# # extend
# _list1.extend(_list2)
# print(_list1)
#
# # insert
# # _list1.insert(2, 'from the other side')
# # print(_list1)
#
#
# def _insert(_list, index, value):
#     final_list = []
#     j = 0
#     #  for i, _value in enumerate(_list):
#     for i in range(len(_list)):
#         if i == index:
#             final_list.append(value)
#             # j -= 1
#         else:
#             final_list.append(_list[j])
#             j += 1
#     return final_list
#
#
# def replace(_list, index, value):
#     final_list = []
#     #  for i, _value in enumerate(_list):
#     for i in range(len(_list)):
#         if i == index:
#             final_list.append(value)
#         else:
#             final_list.append(_list[i])
#     return final_list
#
#
# print(replace(_list1, 2, 'from the other side'))

# set

# numbers = {1, 2, 3, 4, 4, 5, 6, 7, 6}
# numbers = set()
# numbers.add(1)
# numbers.add(1)
# numbers.add(2)
# numbers.add(3)
# #
# # print(numbers[2])
#
# # get rid of every duplicate
# _list = [1, 2, 3, 3, 4, 5, 5]
#
# new_list = set(_list)
# new_list = list(new_list)
#
# print(new_list[1])

# tuple
# k_numbers = (1, 2, 'tuple')
# print(k_numbers[1])

# def _sum(value1, value2, value3):
#
#     addition = value1 + value2 + value3
#     return value1, value2, value3, addition
#
#
# v1, v2, v3, tot = _sum(2, 3, 4)
# print(v2)
#
# values = _sum(2, 3, 4)
# print(values[1])

# dictionary - list of pairs(key -> value)
# _dict = {'first_name': 'evan',
#          'last_name' : 'fisher'}  # dict()
#
# print(_dict['first_name'])
# _dict['age'] = 14
# print(_dict)
# # dont do this - print(_dict['color'])
#
# for k, v in _dict.items():
#     print(k, ':', v)

