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

N,M = map(int,input().split())
pl = [int(i)-1 for i in input().split()]
xl = []
yl = []
for _ in range(M):
    x,y = map(int,input().split())
    xl.append(x-1)
    yl.append(y-1)

UF = UnionFind(N)
for i in range(M):
    x = xl[i]
    y = yl[i]
    UF.union(x,y)
dic1 = UF.all_group_members()
su = 0
for key in dic1:
    members = dic1[key]
    l1 = [pl[member] for member in members]
    su += len(set(l1) & set(members))
print(su)
