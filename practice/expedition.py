import heapq
import numpy as np

N = int(input())
dl = []
fl = []
for _ in range(N):
    d,f = map(int,input().split())
    dl.append(d)
    fl.append(f)
L,P = map(int,input().split())
dl = [L-d for d in dl]
argdl = np.argsort(dl)
dl = [dl[index] for index in argdl]
fl = [fl[index] for index in argdl]
next_pos = P
heap = []
su = 0
for i in range(N):
    if next_pos >= L:
        break
    if dl[i] <= next_pos:
        heapq.heappush(heap, -fl[i])
    else:
        if len(heap) > 0:
            next_pos += heapq.heappop(heap)*(-1)
            heap = []
            su += 1
        else:
            print("-1")
            break
else:
    print(su)
