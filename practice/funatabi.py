import heapq

#startから他の場所までの最短経路
def dijkstra(s):
    #始点sから各頂点への最短距離
    d = [float("inf")] * n
    used = [True] * n #True:未確定
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

n,k = map(int,input().split())
ll = []
edge = [[] for i in range(n)]
#edge[i] : iから出る道の[重み,行先]の配列
for i in range(k):
    l = [int(i) for i in input().split()]
    ll.append(l)
for i in range(k):
    l = ll[i]
    if l[0] == 1:
        edge[l[1]-1].append([l[3],l[2]-1])
        edge[l[2]-1].append([l[3],l[1]-1])
    elif l[0] == 0:
        if dijkstra(l[1]-1)[l[2]-1] == float("inf"):
            print(-1)
        else:
            print(dijkstra(l[1]-1)[l[2]-1])
