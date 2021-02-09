n = int(input())
al = [int(i) for i in input().split()]
print(al.index(min(max(al[:2**(n-1)]),max(al[2**(n-1):])))+1)
