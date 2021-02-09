n = int(input())
hl = [int(i) for i in input().split()]
kaisu = 0
while not(max(hl)) == 0:
    minh = max(hl)
    argmin = len(hl)
    for i,h in enumerate(hl):
        if h != 0 and h <= minh:
            minh = h
            argmin = i
    l = argmin
    r = argmin
    while hl[l] != 0:
        l -= 1
        if l == -1:
            break
    l += 1
    while hl[r] != 0:
        r += 1
        if r == len(hl):
            break
    r -= 1
    for i in range(l,r+1):
        hl[i] -= minh
    kaisu += minh
print(kaisu)
