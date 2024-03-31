import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
costs = [list(map(int,input().split())) for _ in range(N)]
answer = int(1e9)

# 끝부분 색칠하고 시작.
for color in range(3):
    DP = [[int(1e9) for _ in range(3)] for _ in range(N+1)]
    DP[0][color] = 0
    
    for idx in range(1,N+1):
        for idx_color in range(3):
            if idx == 1 and idx_color == color: continue
            if idx == N-1 and idx_color == color: continue
            if idx == N and idx_color != color: continue
            
            for diff_color in range(3):
                if idx_color != diff_color:
                    DP[idx][idx_color] = min(DP[idx][idx_color], costs[idx-1][idx_color] + DP[idx-1][diff_color])
    
    answer = min(answer, DP[-1][0], DP[-1][1], DP[-1][2])
    
print(answer)