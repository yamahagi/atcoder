s = input()
Q = int(input())
#1: normal -1: reverse
cur = 1
leftlist = []
rightlist = []
for _ in range(Q):
    tl = input().split()
    if int(tl[0]) == 1:
        cur *= -1
    else:
        if int(tl[1]) == 1:
            if cur == 1:
                leftlist.append(tl[2])
            else:
                rightlist.append(tl[2])
        else:
            if cur == 1:
                rightlist.append(tl[2])
            else:
                leftlist.append(tl[2])
if cur == 1:
    print(''.join(leftlist[::-1])+s+''.join(rightlist))
else:
    print(''.join(rightlist[::-1])+s[::-1]+''.join(leftlist))
