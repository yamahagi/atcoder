import math

n,m = map(int,input().split())
al = [int(i) for i in input().split()]
al = sorted(al)
beforea = 1
mina = 10**10
if m != 0:
    for i,a in enumerate(al):
        if i == 0:
            if a - beforea != 0:
                mina = min(a-beforea,mina)
        elif a - beforea-1 != 0:
            mina = min(a-beforea-1,mina)
        beforea = a
    if n - al[-1] != 0:
        mina = min(n-al[-1],mina)
    if mina != 10**10:
        su = 0
        beforea = 1
        for i,a in enumerate(al):
            if i == 0:
                su += math.ceil((a-beforea)/mina)
            elif a != beforea:
                su += math.ceil((a-beforea-1)/mina)
            beforea = a
        su += math.ceil((n-al[-1])/mina)
        print(su)
    else:
        print(0)
else:
    print(1)
