import sys

def input(): return sys.stdin.readline()

N = int(input())
matrix = []

for _ in range(N):
    r, c = map(int,input().split())
    matrix.append([r,c])

# DP[i][j] 는 i부터 j까지의 행렬 중 최소 값
DP = [[int(1e9) for _ in range(N)] for _ in range(N)]
for idx in range(N):
    DP[idx][idx] = 0

if N < 2: print(0)
else:
    for gap in range(1,N):
        for prev_idx in range(N-gap):
            next_idx = prev_idx+gap

            for mid_idx in range(prev_idx, next_idx):
                DP[prev_idx][next_idx] = min(DP[prev_idx][next_idx], DP[prev_idx][mid_idx] + DP[mid_idx+1][next_idx] + matrix[prev_idx][0] * matrix[mid_idx][1] * matrix[next_idx][1])
    print(DP[0][N-1])   