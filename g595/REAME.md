## Notes

輸入一個數列，0 表示需要修補的位置，修補的高度是左右比較小的數字，因題目保證不會有連續的 0，所以只要對每一個 0，把它左右較小的數字取出，然後對所有取出的數字加總就可以了。

如果左右邊界是 0 的話，要特別處理，因為左邊界只有右邊鄰居而右邊界只有左邊鄰居。

因要加總，就設一個變數來存其和，這一題完全解有多個數字要判斷，可以用迴圈來處理，但左右邊界不同，把左右邊界單獨處理，其他的位置就用迴圈一起處理。

```python
n = int(input())
h = [int(x) for x in input().split()]
total = 0
if h[0] == 0: total += h[1]
if h[n - 1] == 0: total += h[n - 2]
for i in range(1, n - 1):
    if h[i] == 0: total += min(h[i - 1], h[i + 1])
print(total)
```

另一種更簡潔的寫法。

```python
n = input()
h = [1000] + [int(x) for x in input().split()] + [1000]
total = sum(min(h[i - 1], h[i + 1]) for i in range(1, n + 1) if h[i] == 0)
print(total)
```

## References

- [g595](https://zerojudge.tw/ShowProblem?problemid=g595)
- [吳邦一的APCS題解目錄](https://hackmd.io/@bangyewu/B13lefwMp)
