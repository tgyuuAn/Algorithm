import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
stack = []
answer = 0
for idx in range(N):
    height = int(input())

    while stack and stack[-1][0] < height:
        _, can_see_count = stack.pop()
        answer += can_see_count
        
    if len(stack) == 0:
        stack.append((height, 1))
        continue
    
    elif stack[-1][0] > height:
        answer += 1
        stack.append((height,1))
        
    else:
        _, can_see_count = stack.pop()
        answer += can_see_count
        
        if stack: answer += 1
        
        stack.append((height, can_see_count+1))

print(answer)