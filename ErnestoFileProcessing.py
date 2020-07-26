# read from line
file = open('chat.txt', 'r')
file_content = []
for line in file.readlines():
    line = line.strip()
    line_list = line.split(',')
    print(line_list[2])
    file_content.append(line)
file.close()

# file = open('chat_copy.txt', 'w')
# for line in file_content:
#     file.writelines(line)
# file.close()