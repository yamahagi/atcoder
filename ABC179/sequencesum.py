N,X,M = map(int,input().split())

Al = []
A_syokiti = X
i = 0
A = A_syokiti**2%M
dict1 = {X:1}
Al.append(X)
while A not in dict1:
    dict1[A] = 1
    Al.append(A)
    A = A**2%M
s = Al.index(A)
leng = len(Al[s:])
sumg = sum(Al[s:])
if s > N:
    print(sum(Al[:N]))
else:
    print(sum(Al[:s])+sumg*((N-s)//leng)+sum(Al[s:s+(N-s)%leng]))
