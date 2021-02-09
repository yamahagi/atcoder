import heapq

n,m = map(int,input().split())

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
al = []
bl = []
cl = []
for _ in range(m):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    al.append(a)
    bl.append(b)
    cl.append(c)

edge = [[] for i in range(n)]
mindistl = []
edgedict = [{} for i in range(n)]
#edge[i] : iから出る道の[重み,行先]の配列
heirod = {}
for i in range(n):
    heirod[i] = -1
for i in range(m):
    a = al[i]
    b = bl[i]
    c = cl[i]
    if a == b:
        if heirod[a] == -1:
            heirod[a] = c
        else:
            heirod[a] = min(heirod[a],c)
    else:
        if b not in edgedict[a]:
            edgedict[a][b] = c
        else:
            edgedict[a][b] = min(edgedict[a][b],c)
for a in range(len(edgedict)):
    for b in edgedict[a]:
        edge[a].append([edgedict[a][b],b])
for i in range(n):
    mindistl.append(dijkstra(i))
for i in range(n):
    cost = 10**12
    if heirod[i] != -1:
        cost = heirod[i]
    for (weight,ikisaki) in edge[i]:
        if mindistl[ikisaki][i] != float("inf"):
            cost = min(cost,weight+mindistl[ikisaki][i])
    if cost != 10**12:
        print(cost)
    else:
        print(-1)
