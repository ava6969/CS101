# x = 2
# print(type(x))
# x = 2.5
# print(type(x))
# x = 'a'
# print(type(x))
# x = "evan fisher"
# print(type(x))
# x = True
# print(type(x))

# abels_age = 2
# dewes_age = 3
# evans_age = 7
# number_of_students = 3
#
# average_age = (abels_age + dewes_age + evans_age) / number_of_students

# conditionals - decision making

print('Coding Place for Big Boys')
age = int(input('what is your age: '))

if age >= 18:
    print('Welcome to the Coding Place')
elif age > 15 and age < 18:
    price = int(input('you must pay 5$ to get in >> '))
    if price < 5:
        print('HAHA!! YOU CANNOT COME IN')
    elif price == 5:
        print('Welcome to the Coding Place')
    else:
        print('Welcome!! and you donated', price-5)
else:
    print('Age is not appropriate')


