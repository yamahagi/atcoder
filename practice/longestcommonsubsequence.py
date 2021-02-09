
def accept_input():
    q = int(input())
    Xl = []
    Yl = []
    for _ in range(q):
        Xl.append(input())
        Yl.append(input())
    return q,Xl,Yl
q,Xl,Yl = accept_input()

for x,y in zip(Xl,Yl):
    A = []
    for _ in range(len(x)):
        l = []
        for _ in range(len(y)):
            l.append((0,(-1,-1)))
        A.append(l)
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
    """
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
