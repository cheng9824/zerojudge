def divide(a, b):
    result = abs(a) // abs(b)

    if (a < 0) != (b < 0):
        result = -result

    return result

def modulo(a, b):
    return a - divide(a, b) * b

def calculate():
    global index

    result = 0
    temp = 0

    if line[index] == '(':
        index += 1
        temp = calculate()
    else:
        temp = int(line[index])
        index += 1

    while index < len(line):

        if line[index] == ')':
            index += 1
            result += temp
            return result

        operator = line[index]
        index += 1

        if line[index] == '(':
            index += 1
            number = calculate()
        else:
            number = int(line[index])
            index += 1

        if operator == '*':
            temp *= number
        elif operator == '/':
            temp = divide(temp, number)
        elif operator == '%':
            temp = modulo(temp, number)
        elif operator == '+':
            result += temp
            temp = number
        elif operator == '-':
            result += temp
            temp = -number

    result += temp
    return result

try:
    while True:
        line = input().split()

        index = 0

        result = calculate()

        print(result)

except EOFError:
    pass