n, m = map(int, input().split())
ar = [0 for i in range(n)]
for i in range(n):
    mylist = [int(x) for x in input().split()]
    ar[i] = max(mylist)
s = sum(ar)
print(s)
out = [x for x in ar if s % x == 0]
if len(out) == 0:
    print(-1)
else:
    print(*out)
