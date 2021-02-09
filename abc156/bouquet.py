n,a,b = map(int,input().split())
start = 1
dic1 = {}
dic1inverse = {}
for i in range(n):
    start *= 2
    start %= (10**9+7)
    if start in dic1:
        break
    dic1[start] = i+1
    dic1inverse[i+1] = start
dl = len(list(dic1.keys()))
amari = n % dl
if amari == 0:
    start = dic1inverse[dl]
else:
    start = dic1inverse[amari]
start -= 1
cura = 1
for i in range(a):
    cura *= (n-i)
for i in range(a):
    cura //= (a-i)
curb = 1
for i in range(b):
    curb *= (n-i)
for i in range(b):
    curb //= (b-i)
curc = start - (cura%(10**9+7)) - (curb%(10**9+7))
while curc < 0:
    curc += 10**9+7
