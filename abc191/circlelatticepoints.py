import math

x,y,r = map(float,input().split())
if not(x-r == math.floor(x-r)):
    start = math.floor(x-r) + 1
else:
    start = math.floor(x-r)
end = math.floor(x+r)

ans = 0

for xcur in range(start,end+1):
    absx = abs(x - xcur)
    absy = math.sqrt(r**2 - abs(x - xcur)**2)
    absyplus = math.floor(y + absy)
    if not(y-absy == math.floor(y-absy)):
        absyminus = math.floor(y-absy) + 1
    else:
        absyminus = math.floor(y-absy)
    num = absyplus - absyminus + 1
    ans += num
print(ans)
