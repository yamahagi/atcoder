n = input().split()
xl = [int(i) for i in input().split()]
avexl = sum(xl)/len(xl)
print(min(sum([(x-int(avexl))**2 for x in xl]),sum([(x-(int(avexl)+1))**2 for x in xl])))
