n,k = map(int,input().split())
al = [int(i) for i in input().split()]
dl = [False for _ in range(k+1)]
dl[0] = False
for i in range(1,k+1):
    print(dl)
    for a in al:
        if i - a >= 0 and dl[i-a] == False:
            dl[i] = True
            break
if dl[k]:
    print("First")
else:
    print("Second")
