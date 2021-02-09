n = int(input())
al = [int(i) for i in input().split()]
maxsum_final = 0
for i in range(len(al)):
    mina = 10**6
    maxsum = 0
    for j in range(i,len(al)):
        mina = min(mina,al[j])
        maxsum = max(mina*(j-i+1),maxsum)
    maxsum_final = max(maxsum_final,maxsum)
print(maxsum_final)


