import math
import sys

def input(): return sys.stdin.readline().rstrip()

G = int(input())
square_numbers_set = set()
square_numbers_list = list()
prev = 0
for step in range(1,100_001):
    now = step**2
    if (now-prev) > G: break
    square_numbers_set.add(now)
    square_numbers_list.append(now)
    prev = now

for now in square_numbers_list:
    if now - G in square_numbers_set: print(int(math.sqrt(now)))

# G = 현재 몸무게 ^2 - 원래 몸무게 ^2
# X + G = Y
# G = Y - X