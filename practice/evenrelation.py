import re
import copy
import numpy as np

def accept_input():
    H,W = map(int,input().split())
    S = []
    for _ in range(H):
        S.append(input())
    return H,W,S 
def search(x,y,H,W,S):
    if S[x][y] == "g":
        return 1
    movelist = [(0,1),(0,-1),(1,0),(-1,0)] 
    for move in movelist:
        if x+move[0] == -1 or x + move[0] == H or y+move[1] == -1 or y + move[1] == W:
            continue
        elif visitedlist[x+move[0]][y+move[1]] == 1:
            continue
        elif S[x+move[0]][y+move[1]] == "#":
            continue
        else:
            visitedlist[x+move[0]][y+move[1]] = 1
            if search(x+move[0],y+move[1],H,W,S) == 1:
                return 1
    return 0

H,W,S = accept_input()

#偶数の2頂点に対してまず塗り分けてそっからまた塗っていく:wq

start = (0,0)
end = (0,0)
for i in range(H):
    for j in range(W):
        if S[i][j] == "s":
            start = (i,j)
#幅優先探索
visitedlist = np.zeros((H,W))
result = search(start[0],start[1],H,W,S)
if result == 0:
    print("No")
else:
    print("Yes")
