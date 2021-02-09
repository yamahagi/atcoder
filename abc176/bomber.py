H,W,M = map(int,input().split())
S = []
hl = []
wl = []
for _ in range(M):
    h,w = map(int,input().split())
    hl.append(h)
    wl.append(w)
hdict = {}
wdict = {}
for h,w in zip(hl,wl):
    if h not in hdict:
        hdict[h] = [w]
    else:
        hdict[h].append(w)
    if w not in wdict:
        wdict[w] = [h]
    else:
        wdict[w].append(h)
argmaxh = []
maxh = 0
for key in hdict:
    if len(hdict[key]) > maxh:
        maxh = len(hdict[key])
        argmaxh = [key]
    elif len(hdict[key]) == maxh:
        argmaxh.append(key)
argmaxw = []
maxw = 0
for key in wdict:
    if len(wdict[key]) > maxw:
        maxw = len(wdict[key])
        argmaxw = [key]
    elif len(wdict[key]) == maxw:
        argmaxw.append(key)

