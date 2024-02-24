from collections import deque
import sys

N = int(sys.stdin.readline())
sequence = list(sys.stdin.readline().split())
queries_count = int(sys.stdin.readline())

# i번부터 j번까지는 펠린드롬인가?
DP = [[False for _ in range(N+1)] for _ in range(N+1)]

for idx in range(1,N+1):
    DP[idx][idx] = True

# 짝수면 예를 들어 1~8까지 였을 때에는 4까지 탐색
# 홀수면 예를 들어 1~9까지 였을 때에는 5까지 탐색
for row_idx in range(1,((N+1)//2)):
    now = deque(sequence[row_idx-1])

    for col_idx in range(row_idx-1,0,-1):
        
        # 초기 세팅
        if row_idx == col_idx+1:

            # 짝수 검사
            now.append(sequence[row_idx+(row_idx-col_idx)])
            if now[0] == now[-1]: DP[row_idx][row_idx+(row_idx-col_idx)] = True

            # 홀수 검사
            now.appendleft(sequence[col_idx])
            if now[0] == now[-1]: DP[col_idx][row_idx+(row_idx-col_idx)] = True

        else:
            # 짝수 검사
            now.append(sequence[row_idx+(row_idx-col_idx)])
            if DP[col_idx+2][row_idx+(row_idx-col_idx)-1] == True:
                if now[0] == now[-1]: DP[col_idx+1][row_idx+(row_idx-col_idx)] = True

            now.appendleft(sequence[col_idx])
            if DP[col_idx+1][row_idx+(row_idx-col_idx)-1] == True:
                if now[0] == now[-1]: DP[col_idx][row_idx+(row_idx-col_idx)] = True

print(DP)

for _ in range(queries_count):
    S, E = map(int,sys.stdin.readline().split())
    print(int(DP[S][E]))