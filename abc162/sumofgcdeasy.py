import math
k = int(input())
s = 0
for a in range(1,k+1):
    for b in range(1,k+1):
        for c in range(1,k+1):
            abgcd = math.gcd(a,b)
            abcgcd = math.gcd(abgcd,c)
            s += abcgcd
print(s)
