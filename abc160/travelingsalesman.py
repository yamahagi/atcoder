k,n = map(int,input().split())
al = [int(i) for i in input().split()]
mina = k
for i,a in enumerate(al):
    if i == len(al)-1:
        mina = min((al[i]-al[0]),mina)
    else:
        mina = min(k-(al[i+1]-al[i]),mina)
print(mina)
