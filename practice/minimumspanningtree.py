from heapq import heappush, heappop, heapify

def prime(G,N):
    used = [0]*N
    que = [(c, w) for w, c in G[0]]
    used[0] = 1
    heapify(que)
    ans = 0
    while que:
        cv, v = heappop(que)
        if used[v]:
            continue
        used[v] = 1
        ans += cv
        for w, c in G[v]:
            if used[w]:
                continue
            heappush(que, (c, w))
    return ans

V,E = map(int,input().split())
G = [[] for _ in range(V)]
for i in range(E):
    s,t,w = map(int,input().split())
    G[s].append((t,w))
    G[t].append((s,w))
print(prime(G,V))
