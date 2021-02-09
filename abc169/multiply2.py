n = int(input())
al = [int(i) for i in input().split()]
s = 1
flg = 0
for a in al:
    if flg == 0:
        s *= a
    elif a == 0:
        s *= 0
        flg = 0
    if s > 10**18:
        flg = 1
if flg == 0:
    print(s)
else:
    print(-1)
