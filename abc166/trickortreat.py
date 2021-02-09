n,k = map(int,input().split())
al = []
for _ in range(k):
    d = int(input())
    al1 = [int(i)-1 for i in input().split()]
    al.append(al1)
sundict = {}
for i in range(n):
    sundict[i] = 0
for al1 in al:
    for a in al1:
        sundict[a] = 1
su = 0
for key in sundict:
    if sundict[key] == 0:
        su += 1
print(su)
