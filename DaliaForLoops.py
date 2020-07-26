# while True :
#   run code

# i = 0
# while i <= 10:
#     print(i)
#     i += 1
    # i -= 1

# range(start, stop, step)
# for i in range(0, 11, 1):
#     print(i)

# functions
# define
def sum(x, y):
    z = x + y
    return z


def minimum(x, y):

    if x < y:
        return x
    else:
        return y

def countdown(start, stop):
    # define a base case
    if start == stop:
        return None
    # define a recursive case
    else:
        print(start)
        start -= 1
        return countdown(start, stop)

def evaluate():

    name = input('what is your name? ')
    age = input('what is your age? ')
    return name , age

# call
# countdown(1000, 1)
name, age = evaluate()
print(name)
print(age)