S = input()
T = input()
m = 0
for i in range(0,len(S)-len(T)+1):
    tmp = 0
    for j in range(len(T)):
        if S[i+j] == T[j]:
            tmp += 1
    if m < tmp:
        m = tmp
print(len(T)-m)
