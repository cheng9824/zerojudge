r,c,k,m = map(int, input().split())
p = [[] for i in range(r)]
for i in range(r):
    p[i] = [int(x) for x in input().split()]
temp = [[0]*c for i in range(r)] # working space for next day
for day in range(m): # 從 p 算到 temp
    for i in range(r):
        for j in range(c):
            temp[i][j] = p[i][j]
            if temp[i][j]<0: continue # non-city
            q = p[i][j]//k # move out
            #check 4 neighbors
            if i>0 and p[i-1][j]>=0:
                temp[i][j] += p[i-1][j]//k - q
            if i<r-1 and p[i+1][j]>=0:
                temp[i][j] += p[i+1][j]//k - q
            if j>0 and p[i][j-1]>=0:
                temp[i][j] += p[i][j-1]//k - q
            if j<c-1 and p[i][j+1]>=0:
                temp[i][j] += p[i][j+1]//k - q
    temp, p = p, temp # swap, copy temp back to p
# end for
#output min and max
print(min(p[i][j] for i in range(r)
    for j in range(c) if p[i][j]>=0))
print(max(p[i][j] for i in range(r)
    for j in range(c)))