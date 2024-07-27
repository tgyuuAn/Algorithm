import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
bdg = list(map(int, input().split()))
answer = 0
for idx, height in enumerate(bdg):
    temp_answer = 0
    
    # 왼쪽 먼저 탐색
    left_slope = int(1e9)
    for left_idx in range(idx-1,-1,-1):
        left_height = bdg[left_idx]

        now_slope = (height - left_height) / (idx-left_idx)
        if left_slope > now_slope:
            left_slope = now_slope
            temp_answer += 1

    right_slope = -int(1e9)
    for right_idx in range(idx+1, len(bdg)):
        right_height = bdg[right_idx]

        now_slope = (right_height - height) / (right_idx - idx)
        if right_slope < now_slope:
            right_slope = now_slope
            temp_answer += 1

    answer = max(answer, temp_answer)

print(answer)