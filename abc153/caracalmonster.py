h = int(input())
cur = h
s = 1
while cur != 1:
    cur = cur//2
    s += 1
ans = 0
for i in range(s):
    ans += 2**i
print(ans)
