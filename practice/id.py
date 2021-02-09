n,m = map(int,input().split())
pyl = []
pydict = {}
for _ in range(m):
    p,y = map(int,input().split())
    pyl.append((p,y))
    pydict[p] = []
for (p,y) in pyl:
    pydict[p].append(y)
pydict_sorted = {}
for key in pydict:
    pydict_sorted[key] = {}
    l = pydict[key]
    l.sort()
    for i,y in enumerate(l):
        pydict_sorted[key][y] = i+1
for (p,y) in pyl:
    print("0"*(6-len(str(p)))+str(p)+"0"*(6-len(str(pydict_sorted[p][y])))+str(pydict_sorted[p][y]))
