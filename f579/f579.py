# one
"""
a, b = map(int, input().split())
t = int(input())
ans = 0
for i in range(t):
    l = [int(x) for x in input().split()]
    na = 0; nb = 0
    for x in l:
        if x == a:
            na += 1
        elif x == -a:
            na -= 1
        elif x == b:
            nb += 1
        elif x == -b:
            nb -= 1
    if na > 0 and nb > 0:
        ans += 1
print(ans)
"""

# two
a, b = map(int, input().split())
t = int(input())
ans = 0
for i in range(t):
    l = [int(x) for x in input().split()]
    na = l.count(a) - l.count(-a)
    nb = l.count(b) - l.count(-b)
    if na > 0 and nb > 0:
        ans += 1
print(ans)