import re
import copy

def accept_input():
    H, W = map(int, input().split())
    S = []
    for _ in range(H):
        S.append(input())
    return H,W,S

def process(s):
    if s == "#":
        return 1
    else:
        return 0
H,W,S = accept_input()
new_S = copy.deepcopy(S)
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            new_S[i] = new_S[i][:j]+"#"+new_S[i][j+1:]
        else:
            if i == 0:
                if j == 0:
                    k = process(new_S[i][j+1])+process(new_S[i+1][j+1])+process(new_S[i+1][j])
                elif j == W-1:
                    k = process(new_S[i][j-1])+process(new_S[i+1][j-1])+process(new_S[i+1][j])
                else:
                    k = process(new_S[i][j+1])+process(new_S[i+1][j+1])+process(new_S[i+1][j])+process(new_S[i+1][j-1])+process(new_S[i][j-1])
            elif i == H-1:
                if j == 0:
                    k = process(new_S[i][j+1])+process(new_S[i-1][j+1])+process(new_S[i-1][j])
                elif j == W-1:
                    k = process(new_S[i][j-1])+process(new_S[i-1][j-1])+process(new_S[i-1][j])
                else:
                    k = process(new_S[i][j+1])+process(new_S[i-1][j+1])+process(new_S[i-1][j])+process(new_S[i-1][j-1])+process(new_S[i][j-1])
            else:
                if j == 0:
                    k = process(new_S[i][j+1])+process(new_S[i-1][j+1])+process(new_S[i-1][j])++process(new_S[i+1][j+1])+process(new_S[i+1][j])
                elif j == W-1:
                    k = process(new_S[i-1][j])+process(new_S[i-1][j-1])+process(new_S[i][j-1])+process(new_S[i+1][j])+process(new_S[i+1][j-1])
                else:    
                    k = process(new_S[i][j+1])+process(new_S[i-1][j+1])+process(new_S[i-1][j])+process(new_S[i-1][j-1])+process(new_S[i][j-1])+process(new_S[i+1][j+1])+process(new_S[i+1][j])+process(new_S[i+1][j-1])
            new_S[i] = new_S[i][:j]+str(k)+new_S[i][j+1:]
for l in new_S:
    print(l)
