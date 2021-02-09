n = int(input())
al = [int(i) for i in input().split()]
i = 0
sdict = {}
l = 0
r = 1
while l < len(al):
    start = al[l]
    bin_str = format(start, 'b')
    bin_str = "0"*(20-len(bin_str))+bin_str
    flg = 0
    for i in range(20):
        sdict[19-i] = bin_str[0]
    while flg == 0:

