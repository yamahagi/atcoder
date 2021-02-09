import sys

def accept_input():
    A = input()
    return A

A = accept_input()
if len(A) > 1:
    print(A[:-1])
elif A == "a":
    print(-1)
else:
    print(chr(ord(A)-1))
