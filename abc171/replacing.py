n = int(input())
al = [int(i) for i in input().split()]
q = int(input())
bcl = []
for _ in range(q):
    b,c = map(int,input().split())
    bcl.append((b,c))
adict = {"sum":0}
for i in range(1,10**5+1):
    adict[i] = 0
for i in al:
    adict[i] += 1
    adict["sum"] += i
for (b,c) in bcl:
    if adict[b] == 0:
        print(adict["sum"])
        continue
    adict["sum"] = adict["sum"] -adict[b]*b + adict[b]*c
    print(adict["sum"])
    adict[c] += adict[b]
    adict[b] = 0
