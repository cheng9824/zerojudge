n = int(input())
friend = [int(x) for x in input().split()]
visit = [False] * n
n_group = 0
for i in range(n):
    if visit[i]: continue
    n_group += 1
    visit[i] = True
    p = friend[i]
    while p != i:
        visit[p] = True
        p = friend[p]
print(n_group)