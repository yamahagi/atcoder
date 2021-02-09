import re
import copy
import numpy as np

def accept_input():
    N = int(input())
    xyl = []
    for _ in range(N):
        x,y = map(int,input().split())
        xyl.append((x,y))
    return N,xyl

N,xyl = accept_input()

m2 = 0
for (x,y) in xyl:
    for (x1,y1) in xyl:
        if (x1-x)**2 + (y1-y)**2 > m2:
            m2 =  (x1-x)**2 + (y1-y)**2
print(np.sqrt(m2))
