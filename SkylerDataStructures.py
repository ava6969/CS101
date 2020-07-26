# list() or [] - mutable
# fruits_info = ['orange', 2, 3.5]
# fruit_names = ['apple', 'orange', 'peach']
# fruit_color = []
# fruit_weight = [2.5, 3.5, ]
#
# for fruit_name in fruit_names:
#     print(fruit_name)
# dictionary

# fruit_info = {'name': 'orange',
#               'age': 2,
#               'weight': 3.5} # dict()
#
# # print(fruit_info['age'])
# for fruit, detail in fruit_info.items():
#     print(fruit)
#     print(detail)

# tuple() - immutable
# x = (2, 2.5, 3)
# print(x)
# try:
#     x[1] = 5
# except:
#     print('Type Error')

# set()
# x = {2, 3, 4, 3}
# print(x)

artists = []
max_artists_len = input('Enter max count of artist: ')
i = 1
while len(artists) < int(max_artists_len):
    artist = input('Enter Artist' + str(i) + ': ')
    artists.append(artist)
    i += 1

for artist in artists:
    if artist == 'justin':
        print('You are cool')

print(artists)