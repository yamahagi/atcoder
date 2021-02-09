N,W = map(int,input().split())
wvl = []
wl = []
vl = []
for _ in range(N):
    w,v = map(int,input().split())
    wvl.append((w,v))
    wl.append(w)
    vl.append(v)
vs = sum(vl)+1
dp = []
for i in range(N):
    dpl = []
    for j in range(vs+1):
        dpl.append(10**9+1)
    dp.append(dpl)

for i in range(N):
    if i == 0:
        dp[0][0] = 0
        if wl[0] <= W:
            dp[0][vl[0]] = wl[0]
    else:
        for j in range(vs+1):
            if dp[i-1][j] != 10**9+1:
                dp[i][j] = min(dp[i][j],dp[i-1][j])
                if dp[i-1][j] + wl[i] <= W:
                    dp[i][j+vl[i]] = min(dp[i][j+vl[i]],dp[i-1][j]+wl[i])
for j in range(vs+1):
    if dp[-1][vs-j] != 10**9+1:
        print(vs-j)
        break
