N,Q = ,map(int,input().split())
cl = [int(i) for i in input().split()]
ql = []
for _ in range(Q):
    l,r = map(int,input().split())
    ql.append((l-1,r-1))
dicfromstart = {}
dicfromlast = {}
for i in range(len(cl)):
    if i == 0:
        dicfromstart[i] = {cl[i]:1}
        dicfromlast[len(cl)-1-i] = {cl[i]:1}
    else:
        dicfromstart[i] = dicfromstart[i-1]
        dicfromlast[len(cl)-1-i] = dicfromlast[len(cl)-1-i+1]
        if cl[i] not in dicfromstart[i]:
            dicfromstart[i][cl[i]] = 1
        else:
            dicfromstart[i][cl[i]] += 1
        if cl[i] not in dicfromlast[len(cl)-1-i]:
            dicfromlast[len(cl)-1-i][cl[i]] = 1
        else:
            dicfromslast[len(cl)-1-i][cl[i]] += 1
for (l,r) in ql:
    if l != 0:

