N,M = map(int,input().split())

xyl = []
xydict = {}
for _ in range(M):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    xyl.append((x,y))
    if x in xydict:
        xydict[x].append(y)
    else:
        xydict[x] = [y]

dp = [0 for _ in range(N)]
booll = [False for _ in range(N)]
def f(x):
    if booll[x] == True:
        return dp[x]
    if x not in xydict:
        dp[x] = 0
        booll[x] = True
        return 0
    yl = xydict[x]
    dp[x] = max([f(y) + 1 for y in yl])
    booll[x] = True
    return dp[x]
ans = 0
for i in range(N):
    ans = max(ans,f(i))
print(ans)
