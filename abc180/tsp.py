n = int(input())
xyzl = []
for i in range(n):
    x,y,z = map(int,input().split())
    xyzl.append((x,y,z))
dll = []
for i in range(n):
    f = xyzl[i]
    dl = []
    for j in range(n):
        t = xyzl[j]
        dl.append(abs(t[0]-f[0])+abs(t[1]-f[1])+max(0,t[2]-f[2]))
    dll.append(dl)
dist = dll

memo = {}
def TSP_DP(a, S, b):
    S = S - {a}
    if len(S) == 0:
        memo[(a, tuple(S), b)] = dist[a][b]
        return dist[a][b]
    
    if (a, tuple(S), b) in memo:
        return memo[(a, tuple(S), b)]
    
    d_min = min([dist[a][s] +  TSP_DP(s, S - {s}, b) for s in S])
    memo[(a, tuple(S), b)] = d_min

    return d_min

S = set([])
for i in range(n):
    S.add(i)
print(TSP_DP(0,S,0))

