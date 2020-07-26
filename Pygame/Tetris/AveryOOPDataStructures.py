# DataStructures

cart = [] # list

cart.append('fruits')
cart.append('cereal')

print(cart[0])

result = {}

result['player_1 score'] = 0
result['player_2 score'] = 0
result['player_1 name'] = 'avery'
print(result['player_1 name'])

for item in cart:
    print(item)

for k, v in result.items():
    print('key: {} value: {}'.format(k, v))


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print(self.name, 'is studying')


avery = Student('avery', 14)
avery.study()
print(avery.name)