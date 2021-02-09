N = int(input())
l = []
for _ in range(N):
    a,b = map(int,input().split())
    l.append((a,b))

cur = 0
for i in range(len(l)):
    a,b = l[i]
    if  a == b:
        cur += 1
    else:
        cur = 0
    if cur == 3:
        print("Yes")
        break
else:
    print("No")
