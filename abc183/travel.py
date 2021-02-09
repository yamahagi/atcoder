import itertools

n,k = map(int,input().split())
T = []
for _ in range(n):
    T.append([int(i) for i in input().split()])

list1 = list(itertools.permutations(range(n-1)))
ans = 0
for l in list1:
    su = T[0][l[0]+1]
    for i,tosi in enumerate(l):
        tosit = tosi+1
        if i == len(l)-1:
            su += T[tosit][0]
        else:
            su += T[tosit][l[i+1]+1]
    if su == k:
        ans += 1
print(ans)
