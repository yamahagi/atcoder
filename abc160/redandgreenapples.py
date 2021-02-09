x,y,a,b,c = map(int,input().split())
pl = [(int(i),"r") for i in input().split()]
ql = [(int(i),"g") for i in input().split()]
rl = [(int(i),"w") for i in input().split()]

gn = 0
rn = 0
wn = 0
su = 0
for (i,c) in sorted(pl+ql+rl)[::-1]:
    if c == "r":
        if rn == x:
            continue
        else:
            rn += 1
            su += i
            if gn + rn + wn == x+y:
                break
    elif c == "g":
        if gn == y:
            continue
        else:
            gn += 1
            su += i
            if gn + rn + wn == x+y:
                break
    else:
        wn += 1
        su += i
        if gn + rn + wn == x+y:
            break
print(su)
