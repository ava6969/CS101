print('Welcome to the mall -  buy whatever you want')

# list
cart = [] # list() create an instance of a list

while True:
    item = input('choose an item: ')
    cart.append(item)
    print(item, 'added to cart')
    done = input('Are you done? ')
    if done.lower() == 'yes':
        break

print('Items in cart:')
# for i in range(len(cart)):
#     print('idx:', i, 'item: ', cart[i])

for item in cart:
    print(item)