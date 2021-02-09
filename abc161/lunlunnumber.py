def next(n):
    st = str(n)
    final = ""
    for i in range(len(st)):
        s = st[-i-1]
        if i == len(st)-1:
            if s == "9":
                #最初に1を追加、残りは全部0
                final = "1"+len(st)*"0"
                return final
            else:
                top = str(int(s)+1)
                cur = int(top)
                final = top
                for _ in range(len(st)-1):
                    if cur != 0:
                        cur -= 1
                    final += str(cur)
                return final
        else:
            sprev = st[-i-2]
            if s == "9":
                continue
            elif abs(int(s) + 1 - int(sprev)) >= 2:
                continue
            else:
                top = str(int(s)+1)
                final = st[:-i-1]+top
                cur = int(top)
                for _ in range(i):
                    if cur != 0:
                        cur -= 1
                    final += str(cur)
                return final
k = int(input())
if k <= 10:
    print(k)
else:
    n = 10
    for _ in range(k-10):
        n = next(n)
    print(n)
