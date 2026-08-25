try:
    while True:
        line = input().split()

        temp = int(line[0])

        result = 0

        for i in range(1, len(line), 2):
            operator = line[i]
            number = int(line[i + 1])

            if operator == '*':
                temp *= number
            elif operator == '/':
                temp /= number
            elif operator == '%':
                temp %= number
            elif operator == '+':
                result += temp
                temp = number
            elif operator == '-':
                result += temp
                temp = -number

        result += temp
        print(result)

except EOFError:
    pass