n = int(input())
bikkuril = []
originall = []
for _ in range(n):
    s = input()
    if s[0] == "!":
        bikkuril.append(s[1:])
    else:
        originall.append(s)
dic1 = {}
for s in bikkuril:
    dic1[s] = 1
for s in originall:
    if s in dic1:
        print(s)
        break
else:
    print("satisfiable")
