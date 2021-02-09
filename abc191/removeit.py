n,x = map(int,input().split())
al = [int(i) for i in input().split()]
al = [str(a) for a in al if a != x]
print(' '.join(al))
