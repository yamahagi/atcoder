import re
import copy
import numpy as np

def accept_input():
    N,M = map(int,input().split())
    S = []
    for _ in range(M):
        S.append(map(int,input().split()))
    return N,M,S
def search(node,prev):
    if node not in edgedict:
        return ""
    mode = ""
    for tail in edgedict[node]:
        if tail == prev:
            continue
        elif tail in visited_cur:
            mode = "heiro"
        else:
            visited_cur.append(tail)
            mode_cur = search(tail,node)
            if mode != "heiro":
                mode = mode_cur
    return mode

N,M,S = accept_input()
edgedict = {}
for (head,tail) in S:
    if head not in edgedict:
        edgedict[head] = [tail]
    else:
        edgedict[head].append(tail)
    if tail not in edgedict:
        edgedict[tail] = [head]
    else:
        edgedict[tail].append(head)
visitedlist = []
sumresult = 0
for i in range(1,N+1):
    if i not in visitedlist:
        visited_cur = []
        result = search(i,i)
        if result == "":
            sumresult += 1
        visitedlist.extend(visited_cur)
print(sumresult)
