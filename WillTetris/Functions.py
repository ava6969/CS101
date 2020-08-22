
def check_status(age):
    if age >= 18:
        return 'is adult'
    elif age >= 13:
        return 'is teen'
    else:
        return 'is child'


for _ in range(5):
    age = int(input('enter age'))
    status = check_status(age)
    print(status)
