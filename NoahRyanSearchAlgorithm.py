#problem

# linear search

def linearSearch(_list, word):
    for name in _list:
        if name == word:
            return True
    return False


def remove(_list, word):
    new_list = []

    for name in _list:
        if name != word:
            new_list.append(name)
    return new_list


def insert(_list, index, word):
    new_list = []

    for i in range(len(_list)):
        if i == index:
            new_list.append(word)

        new_list.append(_list[i])
    return new_list


def count(_list, word):
    _count = 0

    for x in _list:
        if x == word:
            _count += 1

    return _count


def main():

    names = ['noah', 'ryan', 'dewe', 'david', 'noah', 'dewe', 'dewe']
    print(count(names, 'dewe'))
    print(names)
    found = linearSearch(names, 'fred')

    new_list = remove(names, 'dewe')
    print(new_list)

    new_list = insert(names, 3, 'names')
    print(new_list)

    if found:
        print('found dewe')
    else:
        print('not found')

main()