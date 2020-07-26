def countdown(start):
    if start <= 0:  # base case
        return None
    else:
        print(start)
        start -= 1
        return countdown(start)


def countdown_arr(start, _list):
    if start == 0:
        _list.append(0)
        return None
    else:
        _list.append(start)
        start -= 1
        return countdown_arr(start, _list)


def countup(stop_num, start=0):

    if start == stop_num:
        return None
    else:
        print(start)
        start += 1
        return countup(stop_num, start)


_list = []
countdown_arr(5, _list)
print(_list)