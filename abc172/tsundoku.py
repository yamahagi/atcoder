n,m,k = map(int,input().split())
al = [int(i) for i in input().split()]
bl = [int(i) for i in input().split()]
bsl = [0]
curs = 0
for b in bl:
    bsl.append(curs+b)
    curs = curs+b
asl = [0]
curs = 0
for a in al:
    asl.append(curs+a)
    curs = curs+a
i = 0
j = m
m = 0
while i <= n and j >= 0:
    start = asl[i]
    while start + bsl[j] > k and j >= 0:
        j -= 1
    if j >= 0:
        m = max(m,i+j)
        i += 1
print(m)
