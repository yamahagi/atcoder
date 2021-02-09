n,w = map(int,input().split())
sdict = {}
tdict = {}
last = 0
for _ in range(n):
    s,t,p = map(int,input().split())
    if s not in sdict:
        sdict[s] = [p]
    else:
        sdict[s].append(p)
    if t not in tdict:
        tdict[t] = [p]
    else:
        tdict[t].append(p)
    last = max(last,t)
water = 0
curw = w
for t in range(last):
    if t in sdict:
       for p in sdict[t]:
           curw -= p
    if t in tdict:
        for p in tdict[t]:
            curw += p
    if curw < 0:
        print("No")
        break
else:
    print("Yes")

