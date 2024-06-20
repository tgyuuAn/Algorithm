import sys

def input(): return sys.stdin.readline().rsrtip()

N, M = map(int, input().split())
trees = list(map(int,input().split()))

def check(mid, trees, target):
    accumulate = 0
    for tree in trees:
        accumulate += max(0, tree-mid)
    
    if accumulate >= target: return True
    return False

left = 0
right= 1_000_000_001
answer = 0
while left+1 < right:
    mid = (left + right)//2

    if check(mid, trees, M):
        answer = mid
        right = mid

    else: left = mid

print(answer)