N = int(input())
su = 0
for i in range(1,N):
    if N%i == 0:
        su += N//i-1
    else:
        su += N//i
print(su)
