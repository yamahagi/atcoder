a,b = map(int,input().split())
al = []
for i in range(1,1251):
    if int(i*0.08) == a:
        al.append(i)
for i in al:
    if int(i*0.1) == b:
        print(i)
        break
else:
    print(-1)
