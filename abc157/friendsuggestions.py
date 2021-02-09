import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

n,m,k = map(int,input().split())
abl = []
adict = [0 for _ in range(n)]
A = [[0]*n for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    abl.append((a,b))
    adict[a] += 1
    adict[b] += 1
    A[a][b] = 1
    A[b][a] = 1
cdl = []
for _ in range(k):
    c,d = map(int,input().split())
    c -= 1
    d -= 1
    cdl.append((c,d))

kk,labels = connected_components(np.array(A))
ldict = [0 for _ in range(max(labels)+1)]
for label in labels:
    ldict[label] += 1
cdict = [0 for _ in range(n)]
for (c,d) in cdl:
    if labels[c] == labels[d]:
        if c not in cdict:
            cdict[c] = 1
        else:
            cdict[c] += 1
        if d not in cdict:
            cdict[d] = 1
        else:
            cdict[d] += 1
s = ""
for i in range(n):
    s += str(ldict[labels[i]] - adict[i] - cdict[i] - 1) + " "
print(s[:-1])
