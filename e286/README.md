## Notes

本題第一個步驟是要計算出兩隊得分，所以設計一個變數儲存主隊的得分，一個變
數儲存客隊的得分。

有兩場比賽，所以這個步驟要執行兩次。

```python
win = 0
a = [int(x) for x in input().split()]
host = sum(a)
a = [int(x) for x in input().split()]
guest = sum(a)
if host > guest:
	win += 1
	print(str(host) + ':' + str(guest))

a = [int(x) for x in input().split()]
host = sum(a)
a = [int(x) for x in input().split()]
guest = sum(a)
if host > guest:
	win += 1
	print(str(host) + ':' + str(guest))

if win == 2: print('Win')
elif win == 0: print('Lose')
else: print('Tie')
```

此外，還要判斷出主隊勝了幾場，題目保證每場比賽一定有勝負，只要計算主隊勝了幾場，就可判斷主隊兩場比賽的結果是勝是負或是平手。為了判斷兩場比賽的結果，除了兩隊總得分之外，還需要一個變數計算主隊的勝場數。

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

使用迴圈架構並合併輸入與加總的指令，可以寫得更簡短一些。

## References

- [e286](https://zerojudge.tw/ShowProblem?problemid=e286)
- [吳邦一的APCS題解目錄](https://hackmd.io/@bangyewu/B13lefwMp)
