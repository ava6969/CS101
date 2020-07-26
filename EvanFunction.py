# define a function
def sum(value_1, value_2):
    '''
    Sum is the name of the function that adds 2 values together
    :param value_1: any integer or float
    :param value_2: any integer or float
    :return: x + y
    '''

    total = value_1 + value_2
    return total


def small(value1, value2):
    #x = value1 if value1 < value2 else value1
    if value1 < value2:
        return value1
    else:
        return value2


minimum = small(2, 4) # call the function
print(minimum)