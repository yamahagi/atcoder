#import numpy as np
import itertools
import queue

def accept_input():
    n = int(input())
    k = int(input())
    al = []
    for _ in range(n):
        al.append(input())
    return n,k,al


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

n,k,al = accept_input()
dict1 = {}
for comb in itertools.permutations(al, k):
    m = "".join(comb)
    dict1[int(m)] = 1
print(len(list(dict1.keys())))
