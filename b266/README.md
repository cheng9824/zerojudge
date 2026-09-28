## Notes

本題是有關矩陣(二維陣列)的操作。

題目定義了兩種操作：翻轉與旋轉，其中翻轉是上下的鏡射，而旋轉是順時針旋轉。題目的給了一連串 M 個操作以及操作後的矩陣，要計算出原來的矩陣為何。就是給了結果求原來的矩陣，而不是給了初始的矩陣求操作後的結果。

對於翻轉，它的逆向操作也是相同的翻轉；對於順時針旋轉，它的逆向操作就是逆時針旋轉；且翻轉不會改變列數與行數，而旋轉後的列數與行數會交換。

首先將輸入讀進來，因為旋轉會改變行數與列數，所以初始化時先讓矩陣的行列數夠大，這題不會超過 10，所以我們用一個 `10 * 10` 的矩陣來做。

```python
r, c, m = map(int, input().split())
mat = [[0] * 10 for x in range(12)]
tem = [[0] * 10 for x in range(12)]
for i in range(r):
    t = [int(x) for x in input().split()]
    for j in range(c):
        mat[i][j] = t[j]
op = [int(x) for x in input().split()]
```

矩陣的上下翻轉相當於將第一列與最後一列對調、第二列與倒數第二列對調，因為每一列都是 mat 的一個元素，我們可以藉由交換（swap）來做。

逆時針的方法是將旋轉後的結果放在一個暫存矩陣中，然後在抄錄回原矩陣。

旋轉後的每一個元素如果是 `tem[j][k]`，那麼它原來是在倒數第 j 個 column（也就是第 `c - 1 - j` 的 column），而原來第 k 列的會跑到第 k 行，也就是 `tem[j][k] = mat[k][c - 1 - j]`。

```python
for opi in op[::-1]:
    if opi == 1:
        for j in range(r // 2):
            mat[j], mat[r - 1 - j] = mat[r - 1 - j], mat[j]
    else:
        for j in range(c):
            for k in range(r):
                tem[j][k] = mat[k][c - 1 - j]
        r, c = c, r
        for j in range(r):
            for k in range(c):
                mat[j][k] = tem[j][k]
```

如何以相反的順序來取得 `op[]` 中的元素（運算）呢？一個是用 `for i in range(m - 1, -1, -1): # op[i] 為要找的運算` 或將 op 倒過來，也就是 `op[::-1]`。這裡採用 reverse 方法。

```python
for i in range(r):
    print(*mat[i][:c])
```

## References

- [b266](https://zerojudge.tw/ShowProblem?problemid=b266)
- [吳邦一的APCS題解目錄](https://hackmd.io/@bangyewu/B13lefwMp)
