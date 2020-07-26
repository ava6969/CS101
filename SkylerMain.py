from Student import Student
from string import punctuation


def custom_range(start, stop, step):

    for i in range(start, stop, step):
        yield i


def main():
    # student = Student('skyler', age=14, height=1.17)
    # student.study()

    # list
    weight1 = [2, 3, 4, 5]
    # weight2 = [w for w in weight1]

    weight2 = [w**i for i, w in enumerate(weight1, start=1)]
    # list comprehension
    # for w in weight1:
    #     weight2.append(w)

    print(weight2)
    # slicing
    # print('index 2:', weight2[2])
    # print('index 1-3:', weight2[1: len(weight2)])
    # print('index 1-3:', weight2[: -1])
    # split
    val = ' Skyler is a smart dude! who cares a lot about, people!!, say ..'
    pre_processed = [c for c in val if c not in punctuation]
    val = ''.join(pre_processed)
    print(val)
    val_arr = val.split(' ')
    print(val_arr)

    # generator
    for i in custom_range(1, 5, 2):
        print(i)

main()