## Notes

判斷輸入的三個正整數是否可以構成三角形，若可構成三角形，則進一步判斷此三角形是直角、銳角或鈍角三角形，且輸出時必須先將輸入的三個數字從小到大輸出，再輸出判斷結果。

## Snippets

```python
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
elif e1 * e1 + e2 * e2 > e3 * e3:
	print("Acute")
```

找出由小到大的三邊長度，可以用 `min()` 和 `max()` 挑出最小值與最大值，中間值可以用總和減去最小與最大值。三角形的判斷就根據流程規劃中的方式來做。

```python
# swap max to c
if a > c:
	a, c = c, a
if b > c:
	b, c = c, b
# swap min to a
if a>b:
	a, b = b, a
print(a, b, c)
```

或是用交換的方式找出最大、最小值。

```python
e = [int(x) for x in input().split()]
e.sort()
# print(e[0], e[1], e[2])
print(*e)
if e[0] + e[1] <= e[2] :
	print('No')
elif e[0] * e[0] + e[1] * e[1] == e[2] * e[2] :
	print('Right')
elif e[0] * e[0] + e[1] * e[1] < e[2] * e[2]:
	print('Obtuse')
else:
	print('Acute')
```

如果會使用 list 與 sort，可以在第 1 行在抓取輸入時直接轉換成數字的 list，在第 2 行將它 `sort()` 排序，然後在第 3 行輸出後比較即可。

## References

- [c294](https://zerojudge.tw/ShowProblem?problemid=c294)
- [吳邦一的APCS題解目錄](https://hackmd.io/@bangyewu/B13lefwMp)
