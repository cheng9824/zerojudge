## Notes

定義 y1 與 y2 分別是 x1 與 x2 的二次函數。對於給定人數 n，要將 n 分成 `n = x1 + x2` 兩個整數，使得 `y1 + y2` 要越大越好。

題目的說明與舉例中，看得出來是要檢查所有 `(x1, x2)` 的可能性，並在其中挑選最大值，所以只要依照題意以迴圈來枚舉嘗試所有可能性就行。

```python
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
n = int(input())

best = -100000000
for x1 in range(n + 1):
	y1 = a[0] * x1 * x1 + a[1] * x1 + a[2]
	x2 = n - x1
	y2 = b[0] * x2 * x2 + b[1] * x2 + b[2]
	best = max(best, y1 + y2)
print(best)
```

這一題的主要架構是枚舉每一種將整數 n 分成兩個整數的可能，對於每一個分割，計算出獲利，在這些獲利中取出最大值。將一個整數 n 分成 x1 與 x2 兩個整數且 `x1 + x2 = n`，我們可以枚舉所有的 x1，然後 `x2 = n - x1`。

## References

- [f312](https://zerojudge.tw/ShowProblem?problemid=f312)
- [吳邦一的APCS題解目錄](https://hackmd.io/@bangyewu/B13lefwMp)
