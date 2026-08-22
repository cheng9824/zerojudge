t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())

    if b - a == c - b == d - c:
        print(f'{a} {b} {c} {d} {(d + (b - a))}')
    else:
        r = b // a
        print(f'{a} {b} {c} {d} {(d * r)}')