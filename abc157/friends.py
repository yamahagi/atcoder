import queue

N,M,K = map(int,input().split())
friendl = []
graph = {}
for i in range(N):
    graph[i] = {}
for _ in range(M):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1
for _ in range(K):
    c,d = map(int,input().split())
    #graph[a-1][b-1] = 1
    #graph[b-1][a-1] = 1
for i in range(N):
    graph[i] = list(graph[i].keys())

def bfs(graph,N):
    seen_list = [False for _ in range(N)]
    seibungoto = []
    for i in range(len(list(graph.keys()))):
        tmp = []
        if seen_list[i] == True:
            continue
        start = list(graph.keys())[i]
        q = queue.Queue()
        q.put(start)
        seen_list[start] = True
        while not q.empty():
            v = q.get()
            tmp.append(v)
            for to in graph[v]:
                if seen_list[to] == False:
                    seen_list[to] = True
                    q.put(to)
        seibungoto.append(tmp)
    return seibungoto

def dfs(graph,N):
    seen_list = [False for _ in range(N)]
    seibungoto = []
    for i in range(len(list(graph.keys()))):
        tmp = []
        if seen_list[i] == True:
            continue
        start = list(graph.keys())[i]
        stack = [start]
        while stack:
            v = stack.pop()
            if seen_list[v] == True:
                continue
            seen_list[v] = True
            tmp.append(v)
            for to in graph[v]:
                if seen_list[to] == False:
                    stack.append(to)
        seibungoto.append(tmp)
    return seibungoto


print(dfs(graph,N))
