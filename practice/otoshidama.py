import re
import copy
import numpy as np

def accept_input():
    N,Y = map(int,input().split())
    return N,Y

N,Y = accept_input()

man_result = -1
gosen_result = -1
sen_result = -1
for man in range(N+1):
    if man*10000 > Y:
        break
    for gosen in range(N+1-man):
        if man*10000 + gosen*5000 > Y:
            break
        elif man*10000+gosen*5000+(N-man-gosen)*1000 == Y:
            man_result = man
            gosen_result = gosen
            sen_result = (N-man-gosen)
            break
    if man_result != -1 or gosen_result != -1 or sen_result != -1:
        break
if man_result != -1 or gosen_result != -1 or sen_result != -1:
    print(str(man_result)+" "+str(gosen_result)+" "+str(sen_result)+" ")
else:
    print(str(man_result)+" "+str(gosen_result)+" "+str(sen_result)+" ")
