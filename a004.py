try:
    while True:
        year = int(input())
        if year % 400 == 0:
            print('閏年')
        elif year % 4 == 0 and year % 100 != 0:
            print('閏年')
        else:
            print('平年')
except EOFError:
    pass