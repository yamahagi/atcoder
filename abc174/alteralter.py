N = int(input())
cl = input()
wsum = 0
rsum = 0
for i in range(len(cl)):
    if cl[i] == "W":
        wsum += 1
    else:
        rsum += 1
curs = rsum
for i in range(rsum):
    if cl[i] == "R":
        curs -= 1
print(curs)
