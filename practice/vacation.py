N = int(input())

al = []
bl = []
cl = []
for _ in range(N):
    a,b,c = map(int,input().split())
    al.append(a)
    bl.append(b)
    cl.append(c)

Al = []
Bl = []
Cl = []
for i in range(N):
    if i == 0:
        Al.append(al[i])
        Bl.append(bl[i])
        Cl.append(cl[i])
    else:
        a = max(Bl[-1]+al[i],Cl[-1]+al[i])
        b = max(Al[-1]+bl[i],Cl[-1]+bl[i])
        c = max(Al[-1]+cl[i],Bl[-1]+cl[i])
        Al.append(a)
        Bl.append(b)
        Cl.append(c)
print(max([Al[-1],Bl[-1],Cl[-1]]))
