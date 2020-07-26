#
# # list comprehension
#
# # numbers = [i for i in range(10)]
# # numbers = [i for i in range(10) if i > 4 ]
# list1 = [1, 3, 4, 5]
#
# list2 = [value for value in list1 if value > 3]
#
# # list2 = []
# # for value in list1:
# #     if value > 3:
# #         list2.append(value)
#
# for i, value in enumerate(list2):
#     print('index {}: {}'.format(i, value))  # print('index:',i,value)
#
# list3 = [('index: {}'.format(i), v) for i, v in enumerate(list1)]
#
# print(list1)
# print(list2)
# print(list3)

# slicing

# print(list1[-1::-1])
# generators
# import random
#
#
# def custom_range(start, end, step):
#     for i in range(start, end, step):
#         yield i
#
#
# def get_batch(_list, batch_size):
#     for i in range(0, len(_list), batch_size):
#         data = _list[i:i+batch_size]
#         yield data
#
#
# _list = [random.randint(0, 10) for _ in range(20)]
#
# for batch in get_batch(_list, 3):
#     print(batch)
#
#

# string manipulation
# name = 'evan! fisher'
# name_list = name.split('!')
# print(name_list)

read_list = []
file = open('chat.txt', 'r')

for line in file.readlines():
    arr = line.strip().split(':')
    read_list.append(arr[-1])
file.close()

file = open('new_chat.txt', 'w')
for line in read_list:
    file.writelines(line+'\n')
file.close()