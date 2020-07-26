# alberto_age = 13
# print(type(alberto_age))

# triangles_area = 25.7
# print(type(triangles_area))

# name = 'alberto saarti'
# print(name)

# is_singing = True
# print(type(is_singing))

# print() helps us display something on our screen
# type() helps us get the data type of a variable

# base = 2
# height = 4
# area = base * height / 2
# print('The area of a triangle is ', area, 'm^2')

base = float(input('enter base: '))
height = float(input('enter height: '))
area = base * height / 2

if area > 100:
    print('this is a large area')
else:
    print('this is a small area')

print('The area of a triangle is ', area, 'm^2')