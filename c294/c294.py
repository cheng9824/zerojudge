a, b, c = map(int, input().split())
e1 = min(a, b, c)
e3 = max(a, b, c)
e2 = a + b + c - e1 - e3
print(e1, e2, e3)

if e1 + e2 <= e3:
    print("No")
elif e1 * e1 + e2 * e2 < e3 * e3:
    print("Obtuse")
elif e1 * e1 + e2 * e2 == e3 * e3:
    print("Right")
else:
    print("Acute")
