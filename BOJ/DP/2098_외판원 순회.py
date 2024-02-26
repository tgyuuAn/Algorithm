import sys

N = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

# 현재 도시가 i이고 이떄까지 방문한 곳은 j
DP = [[int(100) for _ in range(1<<N)] for _ in range(N)]

# 초기화
for i in range(N):
    DP[i][0] = 0

def dfs(now, visited):
    for next in range(N):
        # 똑같은 곳을 가려고 함 ex ) A-> A
        if next == now: continue 
        
        # 이미 갔던 곳을 가려고 함 ex ) A -> B -> A
        if now[next] == "1": continue

        # 갈 수 없는 곳임
        if graph[now][next] == 0: continue

        DP[next][visited | 1 << next] = min(DP[next][visited | 1 << next], DP[now][visited] + graph[now][next])

for i in range(N):
    DP[i][-1] = 0

answer = int(1e9)
for x in range(N):
    answer = min(answer, DP[x][(1<<N)-1])

print(answer)