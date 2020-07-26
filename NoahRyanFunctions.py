# define a function
def add(x, y):
    z = x + y
    return z


def min(x, y):
    if x < y:
        return x
    else:
        return y


def count_up(start,stop):
    # base case
    if start > stop:
        return None
    else:
        print(start)
        start += 1
        return count_up(start, stop)


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


def gcd_loop(a, b):

    while b != 0:
        temp = a
        a = b
        b = temp % b

    return a

def sum_list(_list):

    _sum = 0
    for num in _list:
        _sum += num
    return _sum


def avg_list(_list):

    _sum = 0
    for num in _list:
        _sum += num
    return _sum / len(_list)

# call the function
# x = add(2, 3)
# x = min(6, 5)
# print(x)

# function that seperates odd numbers from even numbers in the list
# print(gcd_loop(60, 48))

print([3, 4, 6, 2, 4])
print(sum_list([3, 4, 6, 2, 4]))
print(avg_list([3, 4, 6, 2, 4]))
# len(_list)