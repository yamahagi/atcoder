import copy

n,m = map(int,input().split())
al = [int(i) for i in input().split()]
edgedict = {}
edgereversedict = {}
for x in range(n):
    edgedict[x] = []
    edgereversedict[x] = []
for _ in range(m):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    if x not in edgedict:
        edgedict[x] = [y]
    else:
        edgedict[x].append(y)
    if y not in edgereversedict:
        edgereversedict[y] = [{x:0}]
    else:
        edgereversedict[y].append({x:0})

visited = [0 for _ in range(n)]
maxl = copy.deepcopy(al)
def rec(i):
    #もし枝がないならその値を返す
    if visited[i] == 1:
        return maxl[i]
    if edgedict[i] == []:
        visited[i] = 1
        return al[i]
    else:
        kouhol = []
        for kouho in edgedict[i]:
            kouhol.append(rec(kouho))
            visited[kouho] = 1
        maxl[i] = max(kouhol)
        return max(maxl[i],al[i])
for i in range(n):
    if visited[i] == 0:
        rec(i)
maxan = 0
for a,max1 in zip(al,maxl):
    if max1 -a > maxan:
        maxan = max1-a
print(maxan)
