# list

cart = ['apple', 'orange', 'banana']

# cart.append('apple')
# cart.append('orange')
# cart.append('banana')
# cart.append('cookies')
# cart.append('meat')

print('old cart = ', cart)
cart[1] = 'turnip'
print('new cart = ', cart)

# tuple
my_info = ('Adedewe', 'Adesola', 'male')
print(my_info)

# set
ages_in_class = {0.1, 0.2, 1, 0.1, 2, 1}
print(ages_in_class)
ages_in_class.add(3)
ages_in_class.add(4)
print(ages_in_class)

# dict
apple = {'fruit_name': 'apple',
         'food_type': 'fruit',
         'color': 'red'}

print(apple['color'])