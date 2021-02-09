import numpy as np
def accept_input():
    N = int(input())
    pl = [int(i) for i in input().split()]
    return N,pl

N,pl = accept_input()
ws = np.sum(pl)
W = ws + 1
A = np.full((N,W),-1)

A[0][0] = 0
A[0][pl[0]] = 0
for i in range(0,N-1):
    for j in range(W):
        if A[i][j] != -1:
            A[i+1][j] = 0
            if j + pl[i+1] < W:
                A[i+1][j+pl[i+1]] = 0
m = 0
for j in range(W):
    if A[-1][j] != -1:
        m += 1
print(m)
