n,k = map(int,input().split())
al = [int(i)-1 for i in input().split()]
matidict = {}
for i in range(n):
    matidict[i] = -1
matil = []
start = 0
i = 0
while matidict[start] == -1:
    matidict[start] = i
    matil.append(start)
    start = al[start]
    i += 1
last = start
prev = matidict[last]
loopl = len(matil)-prev
amari = (k-prev)%loopl
if prev >= k:
    fin = matil[k]+1
else:
    fin = matil[prev+amari]+1
"""
print(matil)
print(last)
print(loopl)
print(prev)
"""
print(fin)
