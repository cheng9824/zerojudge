# one
"""
x = int(input())
d0 = x % 10
d1 = (x // 10) % 10
d2 = (x // 100) % 10
d3 = (x // 1000) % 10
diff = d0 + d2 - d1 - d3
if diff < 0: diff = -diff
print(diff)
"""

# two
"""
x = int(input())
odd = 0
even = 0
i = 0
while x != 0:
    d = x % 10
    if i % 2 == 1:
        odd += d
    else:
        even += d
    x = x // 10
    i += 1

diff = odd - even
if diff < 0: diff = -diff
print(diff)
"""

# three
line = [int(x) for x in input()]
diff = 0
for i in range(len(line)):
    if i % 2: diff += line[i]
    else: diff -= line[i]
print(abs(diff))