import itertools

n,m,q = map(int,input().split())

abcl = []
dl = []
for _ in range(q):
    a,b,c,d = map(int,input().split())
    abcl.append((a-1,b-1,c))
    dl.append(d)
lis = [i for i in range(m)]
m = 0
for pair in itertools.combinations(lis, n):
    print(pair)
    dic1 = {}
    for i,p in enumerate(pair):
        dic1[i] = p
    print(dic1)
    su = 0
    for i,(a,b,c) in enumerate(abcl):
        if dic1[b]-dic1[a] == c:
            su += dl[i]
            print(b)
            print(a)
            print(c)
            print(dl[i])
    print(su)
    m = max(m,su)
print(m)
