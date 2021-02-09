n,C = map(int,input().split())
abcl = []
startl = []
endl = []
for _ in range(n):
    a,b,c = map(int,input().split())
    startl.append((a,c))
    endl.append((b+1,c))
startl = sorted(startl)
endl = sorted(endl)
start = 1
end = 0
cur = startl[0][0]
curc = startl[0][1]
sum1 = 0
while start < len(startl) or end < len(endl):
    if start < len(startl) and startl[start][0] < endl[end][0]:
        sum1 += min(curc,C)*(startl[start][0]-cur)
        cur = startl[start][0]
        curc += startl[start][1]
        start += 1
    else:
        sum1 += min(curc,C)*(endl[end][0]-cur)
        cur = endl[end][0]
        curc -= endl[end][1]
        end += 1
print(sum1)
