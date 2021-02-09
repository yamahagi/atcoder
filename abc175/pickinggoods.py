import heapq


R,C,K = map(int,input().split())
rcl = {}
vd = {}

for i in range(K):
    r,c,v = map(int,input().split())
    if r-1 in rcl:
        rcl[r-1].append(c-1)
        vd[r-1][c-1] = v
    else:
        rcl[r-1] = [c-1]
        vd[r-1] = {c-1:v}

All = []

for i in range(R+1):
    Al = []
    for j in range(C+1):
        Al.append({0:0,1:0,2:0,3:0})
    All.append(Al)
for i in range(R):
    for j in range(C):
        if i in rcl:
            if j in rcl[i]:
               newdyoko = {}
               newdyoko[0] = max(All[i][j][0],All[i][j+1][0])
               for k in range(3):
                   if k == 0 or All[i][j][k] != 0:
                       newdyoko[k+1] = max(All[i][j][k]+vd[i][j],All[i][j][k+1],All[i][j+1][k+1])
                   else:
                       newdyoko[k+1] = 0
               All[i][j+1] = newdyoko
               newdsita = {}
               newdsita[0] = max(All[i+1][j][0],max([All[i][j][key] for key in [0,1,2]])+vd[i][j])
               for k in range(3):
                   newdsita[k+1] = All[i+1][j][k+1]
               All[i+1][j] = newdsita
            else:
                for k in range(4):
                   All[i][j+1][k] = max(All[i][j+1][k],All[i][j][k])
                   All[i+1][j][k] = max(All[i+1][j][k],All[i][j][k])
        else:
            for k in range(4):
                All[i][j+1][k] = max(All[i][j+1][k],All[i][j][k])
                All[i+1][j][k] = max(All[i+1][j][k],All[i][j][k])
print(max(All[R][C-1].values()))
