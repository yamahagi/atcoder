h,w = map(int,input().split())
am = []
for _ in range(h):
    am.append(input())

def dfs(x,y):
    if x == h-1 and y == w-1:
        return 1
    elif x == h-1:
        if am[x][y+1] == "#":
            return 0
        else:
            return dfs(x,y+1)
    elif y == w-1:
        if am[x+1][y] == "#":
            return 0
        else:
            return dfs(x+1,y)
    else:
        if am[x+1][y] == "#":
            if am[x][y+1] == "#":
                return 0
            else:
                return dfs(x,y+1)
        else:
            if am[x][y+1] == "#":
                return dfs(x+1,y)
            else:
                return dfs(x+1,y)+dfs(x,y+1)
dp = []
for x in range(h+1):
    dpl = []
    for j in range(w+1):
        dpl.append(0)
    dp.append(dpl)

for i in range(1,h+1):
    for j in range(1,w+1):
        if i == 1 and j == 1:
            dp[i][j] = 1
            continue
        if am[i-1][j-1] == "#":
            dp[i][j] = 0
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[-1][-1]%(10**9+7))
