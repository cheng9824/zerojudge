import math

a, b, c= map(int, input().split())

D = b ** 2 - 4 * a * c

if D > 0:
    x1 = int((-b + math.sqrt(D)) / (2 * a))
    x2 = int((-b - math.sqrt(D)) / (2 * a))
    print(f'Two different roots x1={x1} , x2={x2}')
elif D == 0:
    x = int(-b / (2 * a))
    print(f'Two same roots x={x}')
else:
    print('No real root')