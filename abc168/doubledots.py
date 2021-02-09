import heapq

#startから他の場所までの最短経路
def dijkstra(s):
    #始点sから各頂点への最短距離
    d = [(float("inf"),s)] * n
    used = [True] * n #True:未確定
    d[s] = (0,s)
    used[s] = False
    edgelist = []
    for e in edge[s]:
        heapq.heappush(edgelist,[e[0],e[1],s])
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        #まだ使われてない頂点の中から最小の距離のものを探す
        if not used[minedge[1]]:
            continue
        v = minedge[1]
        d[v] = (minedge[0],minedge[2])
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                heapq.heappush(edgelist,[e[0]+d[v][0],e[1],v])
    return d

n,m = map(int,input().split())
ll = []
edge = [[] for i in range(n)]
#edge[i] : iから出る道の[重み,行先]の配列
dict1 = {}
for _ in range(m):
    a,b = map(int,input().split())
    a = a-1
    b = b-1
    if a not in dict1:
        dict1[a] = {b:1}
    else:
        dict1[a][b] = 1
    if b not in dict1:
        dict1[b] = {a:1}
    else:
        dict1[b][a] = 1
for a in dict1:
    for b in dict1[a]:
        edge[a].append([1,b])
answer = dijkstra(0)
for a in answer:
    if a[0] == float("inf"):
        print("No")
        break
else:
    print("Yes")
    for i,a in enumerate(answer):
        if i!= 0:
            print(a[1]+1)
"""
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
"""
