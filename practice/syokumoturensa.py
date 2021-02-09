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
        return ' '.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

N,K = map(int,input().split())
xyl = []
tl = []
for i in range(K):
    t,x,y = map(int,input().split())
    xyl.append((x-1,y-1))
    tl.append(t)
UF = UnionFind(3*N)
su = 0
for i in range(K):
    x,y = xyl[i]
    x = x *3
    y = y *3
    t = tl[i]
    if x < 0 or x >= N or y < 0 or y >=N:
        su += 1
        continue
    elif t == 2 and x == y:
        su += 1
        continue
    elif t == 1:
        if UF.same(x,y+1) or UF.same(x,y+2):
            su += 1
            continue
        else:
            UF.union(x,y)
            UF.union(x+1,y+1)
            UF.union(x+2,y+2)
    else:
        if UF.same(x,y) or UF.same(x,y+2):
            su += 1
            continue
        else:
            UF.union(x,y+1)
            UF.union(x+1,y+2)
            UF.union(x+2,y)
print(su)

