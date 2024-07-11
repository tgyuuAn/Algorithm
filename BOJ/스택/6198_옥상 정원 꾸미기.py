import sys
from collections import deque

def input(): return sys.stdin.readline().rstrip()

N = int(input())
stack = []
answer = 0
for _ in range(N):
    now = int(input())

    if not stack:
        stack.append(now)
        continue

    while stack and stack[-1] <= now:
        stack.pop()
    
    answer += len(stack)
    stack.append(now)
    
    
print(answer)