# one
"""
a, b, c = map(int, input().split())
flag = False
if a != 0: la = True
else: la = False
if b != 0: lb = True
else: lb = False
if c != 0: lc = True
else: lc = False
if (la and lb) == lc:
    print('AND')
    flag = True
if (la or lb) == lc:
    print('OR')
    flag = True
if ((la and (not lb )) or ((not la) and lb)) == lc:
    print('XOR')
    flag = True
if not flag: print('IMPOSSIBLE')
"""

# two
a, b, c = map(int, input().split())
flag = False
la = (a != 0)
lb = (b != 0)
lc = (c != 0)
if (la and lb) == lc:
    print('AND')
    flag = True
if (la or lb) == lc:
    print('OR')
    flag = True
if ((la and (not lb)) or ((not la) and lb)) == lc:
    print('XOR')
    flag = True
if not flag: print('IMPOSSIBLE')