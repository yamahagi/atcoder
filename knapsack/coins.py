import math

n = int(input())
pl = [float(i) for i in input().split()]
nl = [0]*(n+1)
for i in range(n):
    p = pl[i]
    if i == 0:
        nl[0] = 1-p
        nl[1] = p
    else:
        newnl = [0]*(n+1)
        for j in range(n+1):
            if j == 0:
                newnl[0] = nl[0]*(1-p)
            else:
                newnl[j] = nl[j-1]*p+nl[j]*(1-p)
        nl = newnl
    """
    print(i)
    print(nl)
    """
su = 0
for i in range(math.ceil((n + 1)/2),n+1):
    su += nl[i]
print(su)
