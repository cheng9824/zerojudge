## Notes

輸入一個正整數，將它的每個位數拆解出來，奇數位數與偶數位數分別相加後，再計算兩者差值的絕對值。

一個整數除以 10 的餘數就是它的個位數字，一個整數除以10的商就是於它右移一位的結果。

```python
x = int(input())
odd = 0
even = 0
i = 0
while x != 0:
	d = x % 10
	if i % 2 == 1:
		odd += d
	else:
		even += d
	x = x // 10
	i += 1

diff = odd - even
if diff < 0: diff = -diff
print(diff)
```

在題目裡，可以每次都求除以 10 的餘數來取出個位數，「除 10 取餘數」這件事不改變，然後去改變資料，每一次將數字右移一位讓下一位數字變成個位數，這樣就可以重複運用「除 10 取餘數」來逐一取出各個位數。

```python
line = [int(x) for x in input()]
diff = 0
for i in range(len(line)):
	if i % 2: diff += line[i]
	else: diff -= line[i]
print(abs(diff))
```

把輸入的數字看成一個字串，字串原本就是字元的陣列，所以只要把每一個數字字元轉換成整數後，利用迴圈將陣列的奇數與偶數分別相加求差值就好了。

## References

- [c290](https://zerojudge.tw/ShowProblem?problemid=c290)
- [吳邦一的APCS題解目錄](https://hackmd.io/@bangyewu/B13lefwMp)
