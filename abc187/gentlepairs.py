n = int(input())
xyl = []
for _ in range(n):
    x,y = map(int,input().split())
    xyl.append((x,y))
su = 0
for i in range(n):
    for j in range(i+1,n):
        x,y = xyl[i][0],xyl[i][1]
        x1,y1 = xyl[j][0],xyl[j][1]
        if (y1 - y)/(x1 - x) >= -1 and (y1 - y)/(x1 - x) <= 1:
            su += 1
print(su)
