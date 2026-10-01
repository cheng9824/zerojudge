n,m,k = map(int, input().split())
q = [[int(x) for x in input().split()] for i in range(n)]
mcost = 100000000 # 設個不可能的大
for case in range(k):
    c = [int(x) for x in input().split()] # city of server
    # quantity from city i to city j
    qq = [[0 for i in range(m)] for j in range(m)]
    for i in range(n): # for each server
        for j in range(m): # server i to city j
            qq[c[i]][j] += q[i][j]
    #end for i,j
    cost = 0
    for i in range(m):
        for j in range(m):
            if i==j:
                cost += qq[i][j]
            elif qq[i][j]<=1000:
                cost += qq[i][j]*3
            else: cost += 1000 + qq[i][j]*2
    mcost = min(mcost,cost)
# end for case
print(mcost)