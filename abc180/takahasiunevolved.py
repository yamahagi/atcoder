x,y,a,b = map(int,input().split())
i = 0
m = 0
while x*(a**i) < y:
    t = i + (y-x*(a**i)-1)//b
    m = max(m,t)
    i += 1
print(m)
