s = input()
t = input()
dp = []
for i in range(len(s)+1):
    dpl = []
    for j in range(len(t)+1):
        dpl.append(0)
    dp.append(dpl)

for i in range(1,len(s)+1):
    for j in range(1,len(t)+1):
        if s[i-1] == t[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
l = max(dp[-1])
cur = 0
sa = ""
i = len(s)
j = len(t)
while l > 0:
    if s[i-1] == t[j-1]:
        sa = s[i-1] + sa
        i -= 1
        j -= 1
        l -= 1
    elif dp[i-1][j] == dp[i][j]:
        i -= 1
    else:
        j -= 1
print(sa)
