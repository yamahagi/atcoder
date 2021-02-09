import numpy as np
import queue

def accept_input():
    H,W = map(int,input().split())
    S = []
    for _ in range(H):
        S.append(input())
    return H,W,S


def widthsearch(q):
    global curvisited
    movelist = [(0,1),(0,-1),(1,0),(-1,0)] 
    lastplace = ((0,0),0)
    cur = 0
    while curvisited < H*W:
        q1 = queue.Queue()
        cur += 1
        while not q.empty():
            pack = q.get()
            y = pack[0][0]
            x = pack[0][1]
            num = pack[1]
            for move in movelist:
                if y+move[0] == -1 or y + move[0] == H or x+move[1] == -1 or x + move[1] == W:
                    continue
                elif visitedlist[y+move[0]][x+move[1]] == 1:
                    continue
                elif S[y+move[0]][x+move[1]] == "#":
                    continue
                else:
                    visitedlist[y+move[0]][x+move[1]] = 1
                    curvisited += 1
                    q1.put(((y+move[0],x+move[1]),num+1))
            if curvisited == H*W:
                break
        q = q1
    return cur

H,W,S = accept_input()
q = queue.Queue()
visitedlist = np.zeros((H,W))
curvisited = 0
for i in range(len(S)):
    for j in range(len(S[i])):
        if S[i][j] == "#":
            q.put(((i,j),0))
            visitedlist[i][j] == 1
            curvisited += 1
#幅優先探索
result = widthsearch(q)
print(result)
