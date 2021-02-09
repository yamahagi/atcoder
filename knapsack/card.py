n,x,y = map(int,input().split())
al = [i for i in input().split()]
bl = [i for i in input().split()]

#y*2 >= xの時は入れ替えるのを優先する
ans = 0
if y *2 >= x:
    i = 0
    while i < n:
        if al[i] == bl[i]:
            i += 1
        elif al[i] != bl[i]:
            if i < n-1  and al[i] != al[i+1] and bl[i] != bl[i+1]:
                ans += x
                i += 2
            else:
                ans += y
                i += 1
else:
    i = 0
    while i < n:
        if al[i] != bl[i]:
            ans += y
            i += 1
        else:
            i += 1
print(ans)

個数*コスト最大値の動的計画法を使うべきだった？
