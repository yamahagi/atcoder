import re
import copy
import numpy as np
import queue

def accept_input():
    R,C = map(int,input().split())
    sy,sx = map(int,input().split())
    gy,gx = map(int,input().split())
    S = []
    for _ in range(R):
        S.append(input())
    return R,C,sy,sx,gy,gx,S


def widthsearch(q):
    movelist = [(0,1),(0,-1),(1,0),(-1,0)] 
    while not q.empty():
        pack = q.get()
        y = pack[0][0]
        x = pack[0][1]
        num = pack[1]
        if S[y][x] == "g":
            return num
        for move in movelist:
            if y+move[0] == -1 or y + move[0] == R or x+move[1] == -1 or x + move[1] == C:
                continue
            elif visitedlist[y+move[0]][x+move[1]] == 1:
                continue
            elif S[y+move[0]][x+move[1]] == "#":
                continue
            else:
                visitedlist[y+move[0]][x+move[1]] = 1
                q.put(((y+move[0],x+move[1]),num+1))

R,C,sy,sx,gy,gx,S = accept_input()
sy = sy-1
sx = sx-1
gy = gy-1
gx = gx-1
for i in range(len(S)):
    if sy == i:
        S[i] = S[i][:sx]+"s"+S[i][sx+1:]
    if gy == i:
        S[i] = S[i][:gx]+"g"+S[i][gx+1:]
    

q = queue.Queue()
q.put(((sy,sx),0))
#幅優先探索
visitedlist = np.zeros((R,C))
visitedlist[sy][sx] = 1
result = widthsearch(q)
print(result)
