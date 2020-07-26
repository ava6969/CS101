import random


def warp(sentence, max_num):

    _words = []
    temp = ''
    for i, char in enumerate(sentence, 1):
        temp += char
        if i % max_num == 0:
            _words.append(temp)
            temp = ''
    return _words


print(warp('if i were a boy, yo uwill listen to her', 3))