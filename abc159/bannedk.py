n = int(input())
al = [int(i) for i in input().split()]
adict = {}
for i,a in enumerate(al):
    if a not in adict:
        adict[a] = [i]
    else:
        adict[a].append(i)
su = 0
alendict = {}
for a in adict:
    alen = len(adict[a])
    alendict[a] = alen
    su += alen*(alen-1)//2
for a in al:
    print(su-(alendict[a]-1))
