import numpy as np
import copy

def accept_input():
    N,D = map(int,input().split())
    return N,D
N,D = accept_input()
five = 0
tmp = D
while tmp % 5 ==0:
    tmp = tmp/5
    five += 1
two = 0
tmp = D
while tmp % 2 ==0:
    tmp = tmp/2
    two += 1
three = 0
tmp = D
while tmp % 3 ==0:
    tmp = tmp/3
    three += 1
A = np.full((2*N+1,2*N+1,N+1),0)
curlist = [(0,0,0)]
A[0][0][0] = 1
for i in range(N):
    A_old = copy.deepcopy(A)
    newlist = []
    for place in curlist:
        twotmp = place[0]
        threetmp = place[1]
        fivetmp = place[2]
        if place not in newlist:
            newlist.append(place)
        if twotmp < 2*N:
            A[twotmp+1][threetmp][fivetmp] += A_old[twotmp][threetmp][fivetmp]
            if (twotmp+1,threetmp,fivetmp) not in newlist:
                newlist.append((twotmp+1,threetmp,fivetmp))
        if twotmp < 2*N-1:
            A[twotmp+2][threetmp][fivetmp] += A_old[twotmp][threetmp][fivetmp]
            if (twotmp+2,threetmp,fivetmp) not in newlist:
                newlist.append((twotmp+2,threetmp,fivetmp))
        if threetmp < 2*N:
            A[twotmp][threetmp+1][fivetmp] += A_old[twotmp][threetmp][fivetmp]
            if (twotmp,threetmp+1,fivetmp) not in newlist:
                newlist.append((twotmp,threetmp+1,fivetmp))
        if twotmp < 2*N and threetmp < 2*N:
            A[twotmp+1][threetmp+1][fivetmp] += A_old[twotmp][threetmp][fivetmp]
            if (twotmp+1,threetmp+1,fivetmp) not in newlist:
                newlist.append((twotmp+1,threetmp+1,fivetmp))
        if fivetmp < N:
            A[twotmp][threetmp][fivetmp+1] += A_old[twotmp][threetmp][fivetmp]
            if (twotmp,threetmp,fivetmp+1) not in newlist:
                newlist.append((twotmp,threetmp,fivetmp+1))
    curlist = newlist
s = 0
for i in range(two,2*N+1):
    for j in range(three,2*N+1):
        for k in range(five,N+1):
            s += A[i][j][k]
all1 = 0
for i in range(0,2*N+1):
    for j in range(0,2*N+1):
        for k in range(0,N+1):
            all1 += A[i][j][k]
print(s/all1)
