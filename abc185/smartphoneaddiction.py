N,m,t = map(int,input().split())
abl = []
for _ in range(m):
    a,b = map(int,input().split())
    abl.append((a,b))

curn = N
curb = 0
for (a,b) in abl:
    curn -= (a-curb)
    if curn <= 0:
        print("No")
        break
    else:
        curn += (b-a)
        curn = min(curn,N)
        curb = b
else:
    curn -= (t-curb)
    if curn <= 0:
        print("No")
    else:
        print("Yes")
