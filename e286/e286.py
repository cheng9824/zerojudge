# one
"""
win = 0
a = [int(x) for x in input().split()]
host = sum(a)
a = [int(x) for x in input().split()]
guest = sum(a)
if host > guest:
    win += 1
print(str(host) + ':' + str(guest))

a = [int(x) for x in input().split()]
host = sum(a)
a = [int(x) for x in input().split()]
guest = sum(a)
if host > guest:
    win += 1
print(str(host) + ':' + str(guest))

if win == 2: print('Win')
elif win == 0: print('Lose')
else: print('Tie')
"""

# two
win = 0
for i in range(2):
    host = sum([int(x) for x in input().split()])
    guest = sum([int(x) for x in input().split()])
    if host > guest: win += 1
    print(host, guest, sep=':')
if win == 2: print('Win')
elif win == 0: print('Lose')
else: print('Tie')