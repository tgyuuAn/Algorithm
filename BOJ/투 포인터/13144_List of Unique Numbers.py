import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
sequence = list(map(int,input().split()))

answer = 0
left = 0
right = 0
temp = set()

while left <= right:
    temp.add(sequence[right])
    
    if len(temp) == right-left+1:   # 중복이 없을 경우,
        
        if right != len(sequence)-1: 
            right += 1
        
        else:
            answer += right-left+1
            if sequence[right] != sequence[left]: temp.discard(sequence[left])
            left += 1
    
    else:                           # 중복이 생겼을 경우,
        answer += right-left
        if sequence[right] != sequence[left]: temp.discard(sequence[left])
        left += 1

print(answer)