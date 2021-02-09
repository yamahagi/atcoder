n,m = map(int,input().split())
al = [int(i) for i in input().split()]
su = sum(al)
ans = 0
for i in range(n):
    if al[i] >= su/(4*m):
        ans += 1
if ans >= m:
    print("Yes")
else:
    print("No")
