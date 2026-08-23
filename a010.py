num = int(input())
factor = 2
result = []

while num > 1:
    count = 0

    while num % factor == 0:
        num = num // factor
        count += 1

    if count > 0:
        if count > 1:
            result.append(f'{factor}^{count}')
        else:
            result.append(f'{factor}')

    factor += 1

print(' * '.join(result))