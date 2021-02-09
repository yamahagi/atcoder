h,n = map(int,input().split())
al = [int(l) for l in input().split()]
if h > sum(al):
    print("No")
else:
    print("Yes")
