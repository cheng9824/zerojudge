# not using bit operation
# 1 =horizontal, 2= vertical, 1+2=3=cross, 0=space 4=pillar
def rem(r, c):
    global m,n # m row, n column
# horizontal
    a[r][c] = 0
    i = c-1
    while i>=0 and (a[r][i]== 1 or a[r][i]==3): # hor or cross
        a[r][i] -= 1
        i -= 1
    i = c+1
    while i<n and (a[r][i]== 1 or a[r][i]==3):
        a[r][i] -= 1
        i += 1
# delete vertical
    i = r-1
    while i>=0 and (a[i][c]== 2 or a[i][c]==3): # vert or cross
        a[i][c] -= 2
        i -= 1
    i = r+1
    while i<m and (a[i][c]== 2 or a[i][c]==3):
        a[i][c] -= 2
        i += 1

def add(r, c):
    global m,n
#vertical
    if a[r][c]!=2 and a[r][c]!=3:
        r2 = r-1
        while r2>=0 and a[r2][c]!=4: r2 -= 1
        if r2 >= 0: # pillar found
            for i in range(r-1,r2,-1):
                a[i][c] += 2 # add vertical
        r2 = r+1
        while r2<m and a[r2][c]!=4: r2+=1
        if r2<m:
            for i in range(r+1,r2,1):
                a[i][c] += 2
# insert horizontal
    if a[r][c]!=1 and a[r][c]!=3:
        c2 = c-1
        while c2>=0 and a[r][c2]!=4: c2-=1
        if c2>=0:
            for i in range(c-1,c2,-1):
                a[r][i] += 1 # add horizontal
        c2 = c+1
        while c2<n and a[r][c2]!=4: c2+=1
        if c2<n:
            for i in range(c+1,c2,1):
                a[r][i] += 1
    a[r][c] = 4
# start main
imax = 0
m,n,h = map(int, input().split())
a = [[0]*n for j in range(m)]
for it in range(h):
    r,c,indel = map(int, input().split())
    if indel == 0: add(r,c)
    else: rem(r,c)
# count total
    total = 0
    for i in range(m):
        total += n - a[i].count(0)
    if total > imax: imax=total
# end it
print(imax)
print(total)