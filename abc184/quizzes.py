n,x = map(int,input().split())
s = input()
for st in s:
    if st == "x":
        if x != 0:
            x-=1
    else:
        x += 1
print(x)
