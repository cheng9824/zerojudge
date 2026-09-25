# one
"""
n = int(input())
for i in range(n):
    p = [int(x) for x in input().split()]
    q = [int(x) for x in input().split()]
    no_error = True
    if p[1] == p[3] or p[1] != p[5] or q[1] == q[3] or q[1] != q[5]:
        print('A', end='')
        no_error = False
    if p[6] != 1 or q[6] != 0:
        print('B', end='')
        no_error = False
    if p[1] == q[1] or p[3] == q[3] or p[5] == q[5]:
        print('C', end='')
        no_error = False
    if no_error:
        print('None')
    else: print()
"""

# two
n = int(input())
for i in range(n):
    p = [0] + [x for x in input().split()]
    q = [0] + [x for x in input().split()]
    ans = ''
    if p[2] == p[4] or p[2] != p[6] or q[2] == q[4] or q[2] != q[6]:
        ans += 'A'
    if p[7] != '1' or q[7] != '0':
        ans += 'B'
    if p[2] == q[2] or p[4] == q[4] or p[6] == q[6]:
        ans += 'C'
    if len(ans) == 0:
        ans = 'None'
    print(ans)