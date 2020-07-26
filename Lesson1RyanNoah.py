# datatype
# integer - 1, 100, 200..
# float - 1.2, 7.6
# boolean - True or False
# string - 'ryan' 'noah' 'x'

# name = 'noah lee'
# print(type(name))

#
# base = float(input('Enter Base: '))
# height = float(input('Enter Height: '))
# area_triangle = base * height * 0.5
# print('the area of the triangle is', area_triangle, 'and of type ', type(area_triangle))

# is_singing = False
age = int(input('What is your age? '))

if age > 18:
    print('Noah and Ryan are above 18 yrs')
elif age == 18:
    print('Noah and Ryan equals 18 yrs')
else:
    print('Noah and Ryan are below 18 yrs')