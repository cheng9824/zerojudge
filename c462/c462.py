k = int(input())
a = input()
uorl = []
for c in a:
    if c >= 'A' and c <= 'Z': uorl.append(0)
    elif c >= 'a' and c <= 'z': uorl.append(1)

seg = []
my_length = 1
for i in range(1, len(uorl)):
    if uorl[i] == uorl[i - 1]:
        my_length += 1
    else:
        seg += [my_length]
        my_length = 1
seg += [my_length]
longest = 0
m = len(seg)
le = 0
while le < m:
    while le < m and seg[le] < k:
        le += 1
    if le >= m: break
    ri = le + 1
    while ri < m and seg[ri] == k:
        ri += 1
    t = (ri - le) * k
    if ri < m and seg[ri] > k:
        t += k
    if t > longest: longest = t
    le = ri
print(longest)