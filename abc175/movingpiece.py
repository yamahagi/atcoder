N,K = map(int,input().split())
Pl = [int(i)-1 for i in input().split()]
Cl = [int(i) for i in input().split()]
dic1= {}
dicgroup = {}
for i in range(N):
    dic1[i] = 10000
start = 0
curi = Pl[start]
group = 0
dicgroup[0] = []
j = 0
for i in range(N):
    if dic1[i] != 10000:
        continue
    else:
        start = i
        dicgroup[group] = []
        dicgroup[group].append(start)
        dic1[i] = group
        curi = Pl[start]
    j = 0
    while curi != start:
        dic1[curi] = group
        dicgroup[group].append(curi)
        curi = Pl[curi]
        j += 1
    group += 1
print(dic1)
print(dicgroup)

for key in dicgroup:
    group = dicgroup[key]
    if len(group) > K:
        
