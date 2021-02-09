class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

N,K,L = map(int,input().split())
Pl = []
Ql = []
Rl = []
Sl = []
for _ in range(K):
    P,Q = map(int,input().split())
    Pl.append(P-1)
    Ql.append(Q-1)
for _ in range(L):
    R,S = map(int,input().split())
    Rl.append(R-1)
    Sl.append(S-1)
UF_road = UnionFind(N)
for i in range(K):
    UF_road.union(Pl[i],Ql[i])
UF_train = UnionFind(N)
for i in range(L):
    UF_train.union(Rl[i],Sl[i])
s  = ""
for i in range(N):
    s += str(len(set(UF_road.members(i)) & set(UF_train.members(i)))) + " "
print(s[:-1])
