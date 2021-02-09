n = int(input())
al = [int(i) for i in input().split()]
bl = [int(i) for i in input().split()]

sum1 = 0
for a,b in zip(al,bl):
    sum1 += a*b
if sum1 == 0:
    print("Yes")
else:
    print("No")
