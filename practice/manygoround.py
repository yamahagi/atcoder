import numpy as np

N,M,L,X = map(int,input().split())
al = [int(i) for i in input().split()]
A = []
for i in range(N):
    Atmp = []
    for j in range(M):
        Atmp.append(100000)
    A.append(Atmp)
A[0][0] = 1
A[0][al[0]%M] = al[0]//M + 1
for i in range(1,N):
    for j in range(M):
        if A[i-1][j] != 100000:
            A[i][j] = min(A[i][j],A[i-1][j])
            A[i][(j+al[i])%M] = min(A[i-1][(j+al[i])%M],A[i][j] + (j+al[i])//M)
for i in range(N):
    if A[i][L] < X:
        print("Yes")
        break
else:
    print("No")
