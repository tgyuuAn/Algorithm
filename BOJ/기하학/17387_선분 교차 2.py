import sys

def input(): return sys.stdin.readline()

x1, y1, x2, y2 = map(int,input().split())
x3, y3, x4, y4 = map(int,input().split())

def CCW(x1, y1, x2, y2, x3, y3):
    result = (x2-x1)*(y3-y1) - (x3-x1) *(y2-y1) 
    if result < 0: return -1
    if result == 0: return 0
    else: return 1

A = CCW(x1, y1, x2, y2, x3, y3) * CCW(x1, y1, x2, y2, x4, y4)
B = CCW(x3, y3, x4, y4, x1, y1) * CCW(x3, y3, x4, y4, x2, y2)
if A == 0 and B == 0: 
    if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):  print(1)
    else: print(0)
elif A <= 0 and B <= 0: print(1)
else: print(0)