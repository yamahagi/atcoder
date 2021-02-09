import copy
n = int(input())
dic1 = {}
sosul = []
alls = 0
for i in range(1,n+1):
    s = 0
    if i == 1:
        alls += 1
    elif i == 2:
        alls += 2*2
        dic1[2] = {2:1}
        sosul.append(2)
    else:
        a = 1
        for sosu in sosul:
            if i %sosu == 0:
                dic1[i] = copy.deepcopy(dic1[i//sosu])
                if sosu in dic1[i]:
                    dic1[i][sosu] += 1
                else:
                    dic1[i][sosu] = 1
                for key in dic1[i]:
                    a *= (dic1[i][key]+1)
                alls += a*i
                break
        else:
            alls += 2*i
            dic1[i] = {i:1}
            sosul.append(i)
print(alls)
