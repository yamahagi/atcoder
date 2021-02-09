h,w = map(int,input().split())
S = []
for _ in range(H):
    S.append(str(input()))
for i in range(H):
    for j in range(W):
        if S[i][j] == "." and ((S[
