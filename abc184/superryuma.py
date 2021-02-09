r1,c1 = map(int,input().split())
r2,c2 = map(int,input().split())
if r1 == r2 and c1 == c2:
    print("0")
elif (abs(r2 - r1) == abs(c2-c1)) or (abs(r2 - r1) + abs(c2 - c1) <= 3):
    print("1")
elif (abs(r2 - r1) + abs(c2 - c1) <= 6) or ((abs(r2-r1) + abs(c2-c1)) % 2 == 0) or (abs(c2 - (c1 + (r2-r1))) <= 3) or (abs(c2- (c1 - (r2 - r1))) <= 3) or  (abs(r2 - (r1 + (c2-c1))) <= 3) or (abs(r2 - (r1 - (c2-c1)) <= 3)):
    print("2")
else:
    print("3")
