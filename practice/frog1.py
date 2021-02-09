N = int(input())
hl = [int(l) for l in input().split()]

al = []
for _ in range(N):
    al.append(10000000000)
al[0] = 0
for i in range(N):
    if i + 1 < N:
        al[i+1] = min(al[i+1],al[i]+abs(hl[i+1]-hl[i]))
    if i + 2 < N:
        al[i+2] = min(al[i+2],al[i]+abs(hl[i+2]-hl[i]))
print(al[-1])
