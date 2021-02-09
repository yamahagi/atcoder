N = int(input())
Al = [int(i) for i in input().split()]

su = sum(Al)
wari = 10**9 + 7
allsu = 0
for i in range(0,N):
    su -= Al[i]
    allsu += (Al[i]*su)
    allsu %= wari
print(allsu)
