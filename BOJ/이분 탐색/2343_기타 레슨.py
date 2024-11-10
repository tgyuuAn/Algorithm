import sys

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
lessons = list(map(int, input().split()))

def check(lessons, mid, M):
    now = 0

    for lesson in lessons:
        if lesson > mid: return False
        
        if mid >= lesson + now:
            now += lesson
        else:
            now = lesson
            M -= 1
            if M < 0: return False
    return True

left = 0
right = 1_000_000_001
answer = 0
while left+1 < right:
    mid = (left + right) // 2
    if (check(lessons, mid, M-1)):
        answer = mid
        right = mid
    else: 
        left = mid

print(answer)