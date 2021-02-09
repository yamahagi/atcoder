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

n,x,y = map(int,input().split())
x -= 1
y -= 1
ll = []
edge = [[] for i in range(n)]
#edge[i] : iから出る道の[重み,行先]の配列
for i in range(n-1):
    edge[i].append([1,i+1])
    edge[i+1].append([1,i])
if [1,y] not in edge[x]:
    edge[x].append([1,y])
if [1,x] not in edge[y]:
    edge[y].append([1,x])
dl = []
for i in range(n):
    d = dijkstra(i)
    dl.append(d)
mindl = [0 for _ in range(n)]
for i in range(n):
    for j in range(i+1,n):
        mindl[dl[i][j]] += 1
for i in range(1,n):
    print(mindl[i])

