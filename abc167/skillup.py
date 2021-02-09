n,m,x = map(int,input().split())
al = []
cl = []
for _ in range(n):
    ac = input().split()
    cl.append(int(ac[0]))
    al.append([int(i) for i in ac[1:]])
l2 = []
for i in range(2**n):
    b_str = format(i, 'b')
    l2.append("0"*(n-len(b_str))+b_str)
minc = sum(cl)+1
for b_str in l2:
    ml = [0 for _ in range(m)]
    c = 0
    for i,b in enumerate(b_str):
        if b == "1":
            for j in range(m):
                ml[j] += al[i][j]
            c += cl[i]
    for m1 in ml:
        if m1 < x:
            break
    else:
        if c < minc:
            minc = c
if minc == sum(cl)+1:
    print(-1)
else:
    print(minc)

