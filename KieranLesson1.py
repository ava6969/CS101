
# data types
# int float str boolean

# x = 'name'
# print(x)
# print(type(x))
#
# x = int(input('enter an integer '))
# y = x / 2
# print('y =', y)
#
# # && ||
# if x > 2 and y < 6:
#     print(1)
#     print(2)
# elif x < 2 or y > 10:
#     print(5)
# else:
#     print(3)

# while x < 5:
#     x += 1
#     print(x)

# for(int i =0; i < 5; ++i) {}

# for i in range(0, 5, 2):
#     print(i)

# for i in range(5):
#     print(i)

info = ['dewe', 24, 2.25]

for i in range(len(info)):
    member = info[i]
    print(member)

for member in info:
    print(member)

for i, member in enumerate(info):
    # print('idx',i,':',member)
    print('idx {}: {}'.format(i, member))

# 0 - dewe
# 1 - 24
# 3 - 2.25

student = {'first_name':'dewe',
           'last name': 'dewe2',
           'age': 3}

print(student['age'])
student['weight'] = 23.3
print(student)

student_set = {22, 3, 2, 3, '4', 6, '4', 3}

items = [2, 4, 5, 2, 4, 2]
items = set(items)

for i in items:
    print(i)

print(items)

print(student_set)

# tuple
student_info = ('kieran', 'barger', 11)
print(student_info[2])


