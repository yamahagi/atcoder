import numpy as np
import itertools
import queue

def accept_input():
    n,m = map(int,input().split())
    al = input().split()
    al = [int(i) for i in al]
    return m,n,al


def dynamic_programming(m,n,S):
    for i in range(0,m):
        if i == 0:
            S[i][0] = 0
            S[i][price[0]*(n//price[0])] = (n//price[0])
        elif i == m-1:
            for j in range(0,n):
                if  S[i-1][j] != 100000:
                    S[i][price[i]*((n-j)//price[i])+j] = min(S[i-1][j]+((n-j)//price[i]),S[i][j])
        else:
            for j in range(0,n):
                if  S[i-1][j] != 100000:
                    S[i][j] = min(S[i-1][j],S[i][j])
                    S[i][price[i]*((n-j)//price[i])+j] = min(S[i-1][j]+((n-j)//price[i]),S[i][price[i]*((n-j)//price[i])+j])
    mi = 100000
    for i in range(m):
        if S[i][n] < mi:
            mi = S[i][n]
    return mi

m,n,al = accept_input()
al.sort(reverse=True)
price = al
S = np.full((m,n+1),100000)
print(price)
print(dynamic_programming(m,n,S))
