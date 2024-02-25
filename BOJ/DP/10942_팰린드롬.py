from collections import deque
import sys

N = int(sys.stdin.readline())
sequence = list(sys.stdin.readline().split())
queries_count = int(sys.stdin.readline())

# i번부터 j번까지는 펠린드롬인가?
DP = [[False for _ in range(N+1)] for _ in range(N+1)]

for idx in range(1,N+1):
    DP[idx][idx] = True

    if idx < N and sequence[idx-1] == sequence[idx]:
        DP[idx][idx+1] = True
        
    if idx > 1 and sequence[idx-1] == sequence[idx-2]:
        DP[idx-1][idx] = True

for count in range(2,N+1):
    for start_idx in range(1,N+1-count):
        end_idx = start_idx+count
        if DP[start_idx+1][end_idx-1] == True and sequence[start_idx-1] == sequence[end_idx-1]:
            DP[start_idx][end_idx] = True
            
for _ in range(queries_count):
    start_idx, end_idx = map(int,sys.stdin.readline().split())
    if DP[start_idx][end_idx]: print(1)
    else: print(0)
