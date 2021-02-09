n,m = map(int,input().split())
al = [int(i) for i in input().split()]

if n - sum(al) >= 0:
    print(n-sum(al))
else:
    print(-1)
