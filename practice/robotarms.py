import numpy as np
import itertools
import queue

def accept_input():
    N = int(input())
    xl = []
    ll = []
    for _ in range(N):
        x,l = map(int,input().split())
        xl.append(x)
        ll.append(l)
    return N,xl,ll


N,xl,ll = accept_input()
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
