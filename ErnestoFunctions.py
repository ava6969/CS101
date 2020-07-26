def addition(x, y):
    sum = x + y
    return sum

#
# def minimum(x, y):
#
#     if x < y:
#         return x
#     else:
#         return y


def maximum(_list):
    max_n = _list[0] # gets first item
    arg_max = 0
    i = 0
    for n in _list:
        if n >= max_n:
            max_n = n
            arg_max = i
        i += 1
    return max_n, arg_max


n, i = maximum([3, 4, 5, 2, 20, 10])
print(n)
print(i)