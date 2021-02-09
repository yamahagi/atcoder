import re
import copy
import numpy as np

def accept_input():
    S = []
    for _ in range(10):
        S.append(input())
    return S
def search(x,y,list1):
    movelist = [(0,1),(0,-1),(1,0),(-1,0)] 
    for move in movelist:
        if x+move[0] == -1 or x + move[0] == 10 or y+move[1] == -1 or y + move[1] == 10:
            continue
        elif visitedlist[x+move[0]][y+move[1]] == 1:
            continue
        elif S_new[x+move[0]][y+move[1]] == "x":
            continue
        else:
            visitedlist[x+move[0]][y+move[1]] = 1
            list1.append((x+move[0],y+move[1]))
            search(x+move[0],y+move[1],list1)
    return list1

S = accept_input()

rikulist = []
for i in range(10):
    for j in range(10):
        if S[i][j] == "o":
            rikulist.append((i,j))
#幅優先探索
result = 0
for i in range(10):
    for j in range(10):
        if S[i][j] == "o":
            continue
        else:
            S_new = copy.deepcopy(S)
            S_new[i] = S_new[i][:j]+"o"+S_new[i][j+1:]
            visitedlist = np.zeros((10,10))
            rikulist_new = search(i,j,[])
            for (x,y) in rikulist:
                if (x,y) not in rikulist_new:
                    break
            else:
                result = 1
                break
    if result == 1:
        break
if result == 0:
    print("NO")
else:
    print("YES")
