# String Manipulation

# i = 0
#
#
# new_line = '\n'
# first_name = 'de,we' + new_line
# # strip
# first_name = first_name.strip()
# print(first_name)
# print('end')

# split
# log = 'DATE YEAR MONTH DESCRIPTION'
# log_list = log.split('')
#
# for l in log_list:
#     print(l)

# read a file

file = open('chat.txt')
splitted = []
for line in file.readlines():
    line = line.strip()
    splitted.append(line)

file.close()

# write to a file
file = open('new_chat', 'w')

for line in splitted:
    file.writelines(line+'\n')

file.close()