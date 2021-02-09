import math
dic1 = {}
n = int(input())
if n == 1:
    print(1)
else:
    su = 0
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            dic1[i] = 1
            dic1[n//i] = 1
    l = list(dic1.keys())
    l.sort()
    for key in l:
        print(key)

