n = int(input())
ll = [int(i) for i in input().split()]
if max(ll) < sum(ll)-max(ll):
    print("Yes")
else:
    print("No")
