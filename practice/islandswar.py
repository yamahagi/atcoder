import numpy as np
import itertools
import queue

def accept_input():
    N,M = map(int,input().split())
    al = []
    bl = []
    for _ in range(M):
        a,b = map(int,input().split())
        al.append(a)
        bl.append(b)
    return N,M,al,bl


N,M,al,bl = accept_input()
tl = [x+l for x,l in zip(xl,ll)]
argtl = np.argsort(tl)
robotl = []
for i in range(N):
    if robotl == []:
        robotl.append(argtl[i])
    else:
        curx = xl[robotl[-1]]
        curl = ll[robotl[-1]]
        if curx+curl <= xl[argtl[i]] - ll[argtl[i]]:
            robotl.append(argtl[i])
print(len(robotl))
