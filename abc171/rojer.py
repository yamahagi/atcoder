import copy
n = int(input())-1
chrdict = {}
for i in range(26):
    chrdict[i] = chr(ord('a')+i)
cur = 26
nagasa = 1
curn = copy.deepcopy(n)
while curn >= cur:
    curn -= cur
    cur *= 26
    nagasa += 1
str1 = ""
for i in range(nagasa):
    str1 = chrdict[curn%26] + str1
    curn = curn//26
print(str1)
