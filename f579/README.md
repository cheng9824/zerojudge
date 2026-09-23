## Notes

對於每一筆清單，要檢查是否 a 與 b 兩種商品皆有購買，最後輸出在多少筆清單中兩種商品皆被購買。

```python
a, b = map(int, input().split())
t = int(input())
ans = 0
for i in range(t):
	l = [int(x) for x in input().split()]
	na = 0; nb = 0
	for x in l:
		if x == a:
		na += 1
		elif x == -a:
		na -= 1
		elif x == b:
		nb += 1
		elif x == -b:
		nb -= 1
	if na > 0 and nb > 0:
		ans += 1
print(ans)
```

商品 a 與 b 是先指定好的，所以對於每一筆清單，我們只要關注 a 與 b 即可，其他商品都可忽略。

商品可能拿進來又移出去，那麼我們可以將拿進來次數減去移出次數來計算淨購買量就可以了。

```python
win = 0
for i in range(2):
	host = sum([int(x) for x in input().split()])
	guest = sum([int(x) for x in input().split()])
if host > guest: win += 1
print(host, guest, sep=':')

if win == 2: print('Win')
elif win == 0: print('Lose')
else: print('Tie')
```

利用 `count()` 函數來計算元素在 list 中出現次數，可以簡化程式碼。

## References

- [f579](https://zerojudge.tw/ShowProblem?problemid=f579)
- [吳邦一的APCS題解目錄](https://hackmd.io/@bangyewu/B13lefwMp)
