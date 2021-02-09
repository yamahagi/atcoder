n = int(input())
dic1 = {}
for _ in range(n):
    dic1[input()] = 1
print(len(list(dic1.keys())))
