n = int(input())
al = []
bl = []
abl = []
diffl = []
for _ in range(n):
    a,b = map(int,input().split())
    al.append(a)
    bl.append(b)
    abl.append((a,b))
    diffl.append(2*a+b)
suma = sum(al)
diffl = sorted(diffl)[::-1]
for i,diff in enumerate(diffl):
    suma -= diff
    if suma < 0:
        print(i+1)
        break
