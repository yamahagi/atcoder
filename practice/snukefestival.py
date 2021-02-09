import bisect

N = int(input())
al = [int(a) for a in input().split()]
bl = [int(b) for b in input().split()]
cl = [int(c) for c in input().split()]

al.sort()
bl.sort()
cl.sort()
su = 0
for b in bl:
    su += bisect.bisect_left(al, b) * (len(cl) - bisect.bisect_right(cl, b))
print(su)
