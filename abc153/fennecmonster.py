n,k = map(int,input().split())
hl = [int(l) for l in input().split()]
hl_sorted = sorted(hl)[::-1]
print(sum(hl_sorted[k:]))
