a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
n = int(input())
best = -100000000
for x1 in range(n + 1):
    y1 = a[0] * x1 * x1 + a[1] * x1 + a[2]
    x2 = n - x1
    y2 = b[0] * x2 * x2 + b[1] * x2 + b[2]
    best = max(best, y1 + y2)
print(best)