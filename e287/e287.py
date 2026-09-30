def next(i,j):
    global mat, m, n
    mm = mat[i][j]
    ni=i; nj=j
    if i>0 and mat[i-1][j]<mm:
        ni=i-1; nj=j; mm=mat[i-1][j]
    if i<m-1 and mat[i+1][j]<mm:
        ni=i+1; nj=j; mm=mat[i+1][j]
    if j>0 and mat[i][j-1]<mm:
        ni=i; nj=j-1; mm=mat[i][j-1]
    if j<n-1 and mat[i][j+1]<mm:
        ni=i; nj=j+1; mm=mat[i][j+1]
    return ni,nj
m, n = map(int, input().split())
oo = 1000001
mat = [[] for i in range(m)]
for i in range(m):
    mat[i] = [int(x) for x in input().split()]
mm = oo
for i in range(m):
    for j in range(n):
        if mat[i][j] < mm:
            si=i; sj=j; mm=mat[i][j]
total = 0
while True:
    total += mat[si][sj]
    mat[si][sj] = oo
    si,sj = next(si,sj)
    if mat[si][sj] == oo:
        break
print(total)