n = int(input())
sl = []
for _ in range(n):
    s = input()
    sl.append(s)
for s in sl:
    dic1 = {"l":{"(":0,")":0},"r":{"(":0,")":0}}
    for st in s:
        if st == "(":
            dic1["r"][")"] += 1
        else:
            if dic1["r"][")"] > 0:
                dic1["r"][")"] -= 1
            else:
                dic1["l"]["("] += 1
    print(s)
    print(dic1)
