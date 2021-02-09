n = int(input())
al = [int(i)-1 for i in input().split()]
adict = {}
for i in range(n):
    adict[i] = 0
for a in al:
    adict[a] += 1
for i in range(n):
    print(adict[i])
