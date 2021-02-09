n = int(input())
sl = []
dic1 = {}
for _ in range(n):
    s = input()
    if s not in dic1:
        dic1[s] = 1
    else:
        dic1[s] += 1
maxs = 0
maxl = []
for key in dic1:
    if dic1[key] > maxs:
        maxs = dic1[key]
        maxl = [key]
    elif dic1[key] == maxs:
        maxl.append(key)
sortl = sorted(maxl)
for l in sortl:
    print(l)
