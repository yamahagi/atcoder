n = int(input())
al = [int(i) for i in input().split()]
adict = {}
for i in range(1,10**6+1):
    adict[i] = 0
for a in al:
    adict[a] += 1
m = max(al)
su = 0
for a in al:
    for i in range(1,1000+1):
        if a%i == 0:
            if a//i == a or i == a:
                if adict[1] >= 1:
                    break
                elif adict[a] > 1:
                    break
            elif adict[a//i] >= 1 or adict[i] >= 1:
                break
    else:
        su += 1
print(su)
