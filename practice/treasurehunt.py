import heapq

#startから他の場所までの最短経路
#O(E logV)
def dijkstra(s,edge):
    #始点sから各頂点への最短距離
    d = [float("inf")] * N
    used = [True] * N #True:未確定
    d[s] = 0
    used[s] = False
    edgelist = []
    for e in edge[s]:
        heapq.heappush(edgelist,e)
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        #まだ使われてない頂点の中から最小の距離のものを探す
        if not used[minedge[1]]:
            continue
        v = minedge[1]
        d[v] = minedge[0]
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                heapq.heappush(edgelist,[e[0]+d[v],e[1]])
    return d

N,M,T = map(int,input().split())
Al = [int(i) for i in input().split()]
edge = [[] for i in range(N)]
edge_inverse = [[] for i in range(N)]
for _ in range(M):
    a,b,c = map(int,input().split())
    edge[a-1].append([c,b-1])
    edge_inverse[b-1].append([c,a-1])

ds = dijkstra(0,edge)
dis = dijkstra(0,edge_inverse)
su = 0
for i in range(N):
    if i == 0:
        su = T*Al[i]
    else:
        if ds[i] == float("inf") or dis[i] == float("inf"):
            continue
        else:
            su = max((T-(ds[i]+dis[i]))*Al[i],su)
print(su)
