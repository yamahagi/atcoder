k = int(input())

start = 7%k
cur = 1
amaridict = {}
for i in range(k):
    if start == 0:
        print(cur)
        break
    else:
        if start in amaridict:
            print(-1)
            break
        else:
            amaridict[start] = 1
            cur += 1
        start = (start * 10 + 7)%k
else:
    if start == 0:
        print(cur)
    else:
        print(-1)
