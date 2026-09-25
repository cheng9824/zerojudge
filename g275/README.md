## Notes

一首七字對聯兩句，每句七個字。

輸入這 14 個字的平仄，0 代表平聲而 1 是仄聲，目標是判斷題目中定義的三個規則有無違反。可以根據定義直接做 0 與 1 的比對來判定即可。

```python
n = int(input())
for i in range(n):
	p = [int(x) for x in input().split()]
	q = [int(x) for x in input().split()]
	no_error = True
	if p[1] == p[3] or p[1] != p[5] or q[1] == q[3] or q[1] != q[5]:
	print('A', end='')
	no_error = False
	if p[6] != 1 or q[6] != 0:
	print('B', end='')
	no_error = False
	if p[1] == q[1] or p[3] == q[3] or p[5] == q[5]:
	print('C', end='')
	no_error = False
	if no_error:
	print('None')
else: print()
```

完全解有 n 首對聯，每一首對聯是各自判斷，所以外層可以用一個迴圈執行 n 次，迴圈的每一次判斷一首對聯。

對於一首對聯，要判斷違反了 ABC 中的哪幾條規則，有違反的規則要依照順序輸出規則編號，且題目要求所有規則都沒有違反時要輸出 None，常用的解決方法是一開始豎立一個旗號，也就是設定一個變數 `no_error = 1`，表示無違反。

在檢查每一條規則時，如果違反就將旗號設為 `no_error = 0`。這樣，最後只要檢查旗號就知道是否都沒有違反。注意編號由 0 開始，與題目的編號差 1。

```python
n = int(input())
for i in range(n):
	p = [0] + [x for x in input().split()]
	q = [0] + [x for x in input().split()]
	ans = ''
	if p[2] == p[4] or p[2] != p[6] or q[2] == q[4] or q[2] != q[6]:
	ans += 'A'
	if p[7] != '1' or q[7] != '0':
	ans += 'B'
	if p[2] == q[2] or p[4] == q[4] or p[6] == q[6]:
	ans += 'C'
	if len(ans) == 0:
	ans = 'None'
print(ans)
```

輸入不一定需要轉換成整數，直接用字串的方式來寫。此外為了可閱讀性，我們在 List 前方放入一個 `[0]`，這樣編號位置就可以跟題目一樣從 1 開始。

輸出是設在一個字串 ans 中，在規則判定時，如果要輸出某一條規則編號時，就將它附加入 ans 的尾端，例如 `ans += 'A'` 就會將 A 放入目前 ans 的字尾，在規則判斷完畢後，我們用  `len(ans)` 就可以知道 ans 是否為空的，如果是空的就要輸出 `None`。

## References

- [g275](https://zerojudge.tw/ShowProblem?problemid=g275)
- [吳邦一的APCS題解目錄](https://hackmd.io/@bangyewu/B13lefwMp)
