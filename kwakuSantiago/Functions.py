


# def mean(x, y):
#
#     res = (x + y ) /2
#
#     return res

def mean(x):

    res = sum(x) / len(x)

    return res


def minimum(x, y):
    # TODO:Code

    if x < y:
        return x
    else:
        return y



z = mean([2, 4, 6])
print(z)

k = minimum(20, 4)
print(k)