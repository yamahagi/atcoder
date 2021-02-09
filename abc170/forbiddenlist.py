x,n = map(int,input().split())
pl = [int(i) for i in input().split()]
pdict = {}
for p in pl:
    pdict[p] = 1
for i in range(100):
    if x - i not in pdict:
        print(x-i)
        break
    if x + i not in pdict:
        print(x+i)
        break
