n = int(input())
abl = []
for _ in range(n):
    a,b = map(int,input().split())
    abl.append((a-1,b-1))
q = int(input())
ql = []
edict = {}
ereversedict = {}
for i in range(n):
    edict[i] = 0
    ereversedict[i] = 0
xsum = 0
for _ in range(q):
    t,e,x = map(int,input().split())
    if t == 1:
        edict[e] += x
    else:
        ereversedict[e] += x
    xsum += x
nodecost = [xsum for _ in range(n)]

