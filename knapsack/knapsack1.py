N,W = map(int,input().split())
wvl = []
for _ in range(N):
    w,v = map(int,input().split())
    wvl.append((w,v))
nwl = []
for _ in range(N):
    nwll = []
    for _ in range(W+1):
        nwll.append(-1)
    nwl.append(nwll)
for i,(w,v) in enumerate(wvl):
    if i == 0:
        nwl[0][0] = 0
        nwl[0][w] = v
    else:
        for j in range(W+1):
            if nwl[i-1][j] != -1:
                nwl[i][j] = max(nwl[i-1][j],nwl[i][j])
                if j + w <= W:
                    nwl[i][j+w] = max(nwl[i-1][j]+v,nwl[i][j])
m = max(nwl[-1])
print(m)
