
def accept_input():
    q = int(input())
    Xl = []
    Yl = []
    for _ in range(q):
        Xl.append(input())
        Yl.append(input())
    return q,Xl,Yl
N = int(input())
cl = []
al = []
for _ in range(N):
    cl.append(int(input()))
    al.append(1000000)
for i in range(N):
    for j in range(N):
        if j == 0:
            if cl[i] < al[0]:
                al[0] = cl[i]
                break
        else:
            if cl[i] < al[j]:
                al[j] = cl[i]
                break
for i in range(N):
    if al[i] == 1000000:
        print(N-i)
        break
else:
    print(0)
"""
for i in range(len(x)):
    if i == 0:
        for j in range(len(y)):
            if x[i] == y[j]:
                if j == 0:
                    A[i][j] = (1,(-1,-1))
                else:
                    A[i][j] = (1,(i,j-1))
            else:
                if j != 0:
                    A[i][j] = (A[i][j-1][0],(i,j-1))
        continue
    for j in range(len(y)):
        if x[i] == y[j]:
            if j == 0:
                A[i][j] = (1,(-1,-1))
            else:
                if A[i-1][j-1][0] + 1 > A[i][j-1][0]:
                    A[i][j] = (A[i-1][j-1][0]+1,(i-1,j-1))
                else:
                    A[i][j] = (A[i][j-1][0],(i,j-1))
        else:
            if j != 0:
                if A[i-1][j][0]  > A[i][j-1][0]:
                    A[i][j] = (A[i-1][j][0],(i-1,j))
                else:
                    A[i][j] = (A[i][j-1][0],(i,j-1))
i = len(A)-1
j = len(A[0])-1
print(A[i][j][0])
s = ""
while True:
    if A[i][j][0] == 0:
        break
    elif A[i][j][1]  == (-1,-1):
        s += x[i]
        break
    newplace = A[i][j][1]
    if A[i][j][0] != A[newplace[0]][newplace[1]][0]:
        s += x[i]
    i = newplace[0]
    j = newplace[1]
print(s)
print(len(s))
"""
