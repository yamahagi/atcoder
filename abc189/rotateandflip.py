n = int(input())
xyl = []
for _ in range(n):
    x,y = map(int,input().split())
    xyl.append((x,y))
m = int(input())
opl = []
for _ in range(m):
    op = input()
    opl.append(op)
q = int(input())
abl = []
for _ in range(q):
    a,b = map(int,input().split())
    b -= 1
    abl.append((a,b))
A = [[1,0],[0,1]]
b = [0,0]
Abl = []
Abl.append((A,b))
for i in range(m):
    op = opl[i]
    if op[0] == "1":
        A = [[A[1][0],A[1][1]],[-A[0][0],-A[0][1]]]
        b = [b[1],-b[0]]
    elif op[0] == "2":
        A = [[-A[1][0],-A[1][1]],[A[0][0],A[0][1]]]
        b = [-b[1],b[0]]
    elif op[0] == "3":
        p = int(op[2:])
        A = [[-A[0][0],-A[0][1]],[A[1][0],A[1][1]]]
        b = [-b[0]+2*p,b[1]]
    else:
        p = int(op[2:])
        A = [[A[0][0],A[0][1]],[-A[1][0],-A[1][1]]]
        b = [b[0],-b[1]+2*p]
    Abl.append((A,b))
for (a,b) in abl:
    x,y = xyl[b][0],xyl[b][1]
    A,b = Abl[a][0],Abl[a][1]
    xy = [A[0][0]*x+A[0][1]*y+b[0],A[1][0]*x+A[1][1]*y+b[1]]
    x = xy[0]
    y = xy[1]
    print(str(x) + " " + str(y))
