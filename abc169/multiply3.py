al = input().split()
a = int(al[0])
b = int(al[1][:-3])*100+int(al[1][-2:])
if len(str(a**b)) <= 2:
    print(0)
else:
    print(str(a*b)[:-2])
