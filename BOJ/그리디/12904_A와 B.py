import sys

def input(): return sys.stdin.readline().rstrip()

S = list(input())
T = list(input())

while len(T) > len(S):
    if T[-1] == "A": T.pop()
    else:
        T.pop()
        T = T[::-1]

if S == T: print(1)
else: print(0)