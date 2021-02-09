import math
n = int(input())
xl = [abs(int(i)) for i in input().split()]
print(sum(xl))
su = 0
for x in xl:
    su += x**2
print(math.sqrt(su))
print(max(xl))
