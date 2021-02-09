n,k = map(int,input().split())

su = 0
for i in range(k,n+2):
    start = (i-1)*i//2
    end = n*(n+1)//2-(n-i)*(n-i+1)//2
    su += end-start+1
print(su%(10**9+7))
