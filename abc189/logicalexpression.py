n = int(input())
sl = []
for _ in range(n):
    sl.append(input())


def recursiveSAT(sl):
    if len(sl) == 1:
        s = sl[0]
        if s == "AND":
            return 1
        else:
            return 3
    else:
        s = sl[-1]
        if s == "AND":
            return recursiveSAT(sl[:-1])
        else:
            return 2**len(sl) + recursiveSAT(sl[:-1])
print(recursiveSAT(sl))
