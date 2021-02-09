import math
a,b,c,d = map(int,input().split())
tk = math.ceil(c/b)
ak = math.ceil(a/d)
if tk <= ak:
    print("Yes")
else:
    print("No")
