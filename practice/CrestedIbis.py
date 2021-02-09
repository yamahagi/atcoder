import numpy as np

N,W = map(int,input().split())
vl = []
wl = []
vwl = []
for _ in range(N):
    v,w = map(int,input().split())
    vl.append(v)
    wl.append(w)
    vwl.append(v/w)
A = np.full((N,W+1),-1)
A[0][0] = 0
if wl[0] <= W:
    for j in range(((W-0)//wl[0])+1):
        A[0][wl[0]*j] = max(A[0][wl[0]*j],A[0][0]+vl[0]*j)
for i in range(1,N):
    for j in range(W+1):
        if A[i-1][j] != -1:
            A[i][j] = max(A[i][j],A[i-1][j])
            if j + wl[i] <= W:
                A[i][j+wl[i]] = max(A[i][j+wl[i]],A[i-1][j]+vl[i])
print(max(A[-1]))
