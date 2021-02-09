n,m = map(int,input().split())
xl = [int(i) for i in input().split()]
xl.sort()
xlaida = []
for i in range(len(xl)-1):
    xlaida.append(xl[i+1]-xl[i])
xlaida.sort()
su = sum(xlaida)
if n >= len(xl):
    print(0)
else:
    for i in range(1,n):
        su -= xlaida[-i]
    print(su)
