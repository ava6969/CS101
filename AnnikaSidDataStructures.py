# tuple, dict, sets

# tuple

# my_info = ('dewe', 22, 1997)
# print(my_info[0])
# print(my_info[1])
# print(my_info[2])

# set
# _set = {2, 3, 4,3, 5, 1,2,2}
# print(_set)
#
# sentence = ' i am dewe, i love to watch movies and i play games and i ..'
# sent_list = sentence.split()
# sent_set = set(sent_list)
# sent_list = list(sent_set)
#
# for sent in sent_list:
#     print(sent)
#
# _dict = {'name': 'adedewe adesola',
#          'age' : 22,
#          'year': 1997}
#
# print(_dict['year'])
#

sentence = input(' type anything?\n')

_dict = {}
sent_list = sentence.split()

for word in sent_list:

    if word in _dict.keys():
        _dict[word] += 1
    else:
        _dict[word] = 1

for k, v in _dict.items():

    print('{} : {}'.format(k, v))