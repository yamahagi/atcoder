n = int(input())
al = [int(i) for i in input().split()]
al.sort()
print(sum(al[1:]))
