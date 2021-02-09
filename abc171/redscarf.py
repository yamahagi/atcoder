n = input()
al = [int(i) for i in input().split()]
for i,a in enumerate(al):
    if i == 0:
        cur = a
    else:
        cur = cur^a
sl = []
for a in al:
    sl.append(str(cur^a))
print(' '.join(sl))
