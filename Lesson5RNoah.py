# list
cart = []

cart.append('orange')
cart[0] = 'dewe'
print(cart)

# tuple
name = ('ryan', 'noah', 'lee')
print(name[2])

# set
new_cart = {'apple', 'oranges', 'oranges', 'strawberries', 1, 3, 1}
# convert a set to list
new_cart_list = list(new_cart)
print(new_cart_list[0])

# dict
student = {'name': 'Adedewe Adesola',
           'age' : 80,
           'height': 9.5}
print(student['height'])
print(student.keys())
print(student.values())
