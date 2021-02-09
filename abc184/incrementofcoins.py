import numpy as np

A,B,C = map(int,input().split())
ABCL = np.zeros((101,101,101,298-(A+B+C)+1))
"""
ABCL = []
for _ in range(102):
    ABCLL = []
    for _ in range(102):
        ABCLLL = []
        for _ in range(102):
            ABCLLLL = []
            for _ in range(298-(A+B+C)+1):
                ABCLLLL.append(0)
            ABCLLL.append(ABCLLLL)
        ABCLL.append(ABCLLL)
    ABCL.append(ABCLL)
"""
print("done")
ABCL[A][B][C][0] = 1
for su in range(0,298-(A+B+C)):
    for a in range(A,100):
        for b in range(B,100):
            for c in range(C,100):
                if ABCL[a][b][c][su] != 0:
                    ABCL[a+1][b][c][su+1] += ABCL[a][b][c][su] * (a/(a+b+c))
                    ABCL[a][b+1][c][su+1] += ABCL[a][b][c][su] * (b/(a+b+c))
                    ABCL[a][b][c+1][su+1] += ABCL[a][b][c][su] * (c/(a+b+c))
kitaiti = 0
for su in range(0,298-(A+B+C)+1):
    for a in range(A,101):
        for b in range(B,101):
            for c in range(C,101):
                if c == 100 and ABCL[a][b][c][su] != 0:
                    kitaiti += ABCL[a][b][c][su] * su
                elif b == 100 and ABCL[a][b][c][su] != 0:
                    kitaiti += ABCL[a][b][c][su] * su
                elif a == 100 and ABCL[a][b][c][su] != 0:
                    kitaiti += ABCL[a][b][c][su] * su
print(kitaiti)


