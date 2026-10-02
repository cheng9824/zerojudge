m,n,k = map(int,input().split())
bomb = [[0]*n for i in range(m)]
monster = [] # (r,c,dr,dc)
for i in range(k):
    monster.append([int(x) for x in input().split()])
# input complete
while len(monster)>0:
# check explosion, alive monster save in temp
    temp = []
    for p in monster:
        if bomb[p[0]][p[1]]:
            bomb[p[0]][p[1]] = -1 # explode
        else:
            temp.append(p)
#end for p
    monster, temp = temp, monster
# clear exploded bomb
    for i in range(m):
        for j in range(n):
            if bomb[i][j] == -1:
                bomb[i][j] = 0
# move monster
    temp=[] # keep inside monster
    for p in monster:
        bomb[p[0]][p[1]] = 1
        p[0] += p[2]
        p[1] += p[3]
        if 0<= p[0] <m and 0<= p[1]<n:
            temp.append(p)
# end for
    monster, temp = temp, monster
# end while
ans = sum(bomb[i][j] for i in range(m) for j in range(n))
print(ans)