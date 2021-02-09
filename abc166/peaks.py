n,m = map(int,input().split())
hl = [int(i) for i in input().split()]
abl = []
abdict = {}
for i in range(n):
    abdict[i] = {}
for i in range(m):
    a,b = map(int,input().split())
    abl.append((a-1,b-1))
    abdict[a-1][b-1] = 1
    abdict[b-1][a-1] = 1
su = 0
for a in abdict:
    for b in abdict[a]:
        if hl[a] <= hl[b]:
            break
    else:
        su += 1
print(su)
