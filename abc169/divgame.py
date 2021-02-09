import math
import copy
n = int(input())
flg = 0
curn = copy.deepcopy(n)
dict1 = {}
for i in range(2,int(math.sqrt(n))+1):
    if curn%i == 0:
        curm = 0
        while curn%i == 0:
            curn = curn//i
            curm += 1
        dict1[i] = curm
if dict1 == {}:
    if n == 1:
        print(0)
    else:
        print(1)
else:
    su = 0
    for key in dict1:
        curm = dict1[key]
        for i in range(1,curm+1):
            if i*(i+1)/2 <= curm and (i+1)*(i+2)/2 > curm:
                su += i
                break
    print(su)

