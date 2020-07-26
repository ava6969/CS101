
# operations
# int/float => + / * -
# bool => and or
# x = int(input('Enter x: '))
# and returns True if all the statements are Trtruth = x > 2 and x < 10
# # print(type(truth))
# # print(truth)ue
#

# if x > 2 and x < 10:
#     print('x > 2 and x < 10')
# elif x > 10 and x < 200:
#     print('x > 10 and x < 200')
# elif x == 1 or x > 200:
#     print(x)
# else:
#     print('x <= 2')

print('Welcome to the Park')

name = input('Enter Name: ')
age =  input('Enter Age: ')
payment = input('Enter Payment: ')

VIP = False

if int(payment) >= 100:
    VIP = True

if int(age) > 18:
    print(name, 'is an adult of age', age)
elif int(age) >= 13 and int(age) < 18:
    print(name, 'is a teen of age', age)
else:
    print(name, 'is a kid')

if VIP:
    print('Has VIP Access')
else:
    print('Does not Have VIP Access')


# you cant start the decision block with and elif or else statement , has to be an if statement
