# one
n = int(input())
h = [int(x) for x in input().split()]
total = 0
if h[0] == 0: total += h[1]
if h[n - 1] == 0: total += h[n - 2]
for i in range(1, n - 1):
    if h[i] == 0: total += min(h[i - 1], h[i + 1])
print(total)

# two
"""
n = input()
h = [1000] + [int(x) for x in input().split()] + [1000]
total = sum(min(h[i - 1], h[i + 1]) for i in range(1, n + 1) if h[i] == 0)
print(total)
"""