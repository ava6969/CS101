
# list
# print('Welcome to the super supermarket')
# while True:
#     item = input('what item do you want ')
#     print('you added', item)
#     cart.append(item)
#     done = input('Are you done? ')
#     if done == 'yes':
#         break
#
# print('you have to pay for', cart)

# i = 0
# while i <= 5:
#     print(i)
#     i += 1

# for i in range(0, 5):
#     print(i)
#
# for i in range(5, 0, -1):
#     print(i)

# cart = ['cereal', 'apple', 'pineapple']
# # print('idx 1 =', cart[1])

# TASK
# ASK YOURSELF TO INPUT 4 NUMBERS IN A LOOP
# PRINT OUT THE 4 NUMBERS

n_list = [1, 2, 4, 65]
# print(min(n_list))
# print(max(n_list))
# print(len(n_list)) # gives the size of the list


for i in range(0, len(n_list)):
    print('idx',i,':',n_list[i])

for number in n_list:
    print(number)