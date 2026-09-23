## Notes

本題給了三種邏輯二元運算的真值表，輸入 a, b, r，問你「若 a X b = r，則 X 可能是三種運算中的哪幾種。」題目中所列的三種運算是真實的 AND, OR 與 XOR。

先輸入 a, b, r，再依照題目給的運算順序逐一判斷是否滿足運算的要求，如果都不滿足，要輸出 IMPOSSIBLE。

```python
a, b, c = map(int, input().split())
flag = False
if a != 0: la = True
else: la = False
if b != 0: lb = True
else: lb = False
if c != 0: lc = True
else: lc = False
if (la and lb) == lc:
	print('AND')
	flag = True
if (la or lb) == lc:
	print('OR')
	flag = True
if ((la and (not lb )) or ((not la) and lb)) == lc:
	print('XOR')
	flag = True
if not flag: print('IMPOSSIBLE')
```

如果想要知道在某一段運算之中是否曾經發生過某事件，可以在進入這一段之前先設立一個旗標變數為 False，在運算過程中只要該事件發生就將旗標設為 True。

```python
a, b, c = map(int, input().split())
flag = False
la = (a != 0)
lb = (b != 0)
lc = (c != 0)
if (la and lb) == lc:
	print('AND')
	flag = True
if (la or lb) == lc:
	print('OR')
	flag = True
if ((la and (not lb)) or ((not la) and lb)) == lc:
	print('XOR')
	flag = True
if not flag: print('IMPOSSIBLE')
```

a 是否不為 0 這件事也可以用以上的簡化寫法。

## References

- [c461](https://zerojudge.tw/ShowProblem?problemid=c461)
- [吳邦一的APCS題解目錄](https://hackmd.io/@bangyewu/B13lefwMp)
