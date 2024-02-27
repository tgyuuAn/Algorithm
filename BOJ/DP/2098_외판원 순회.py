import sys

N = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

# 현재 도시가 i이고 이떄까지 방문한 곳은 j
DP = [[-1 for _ in range(1<<N)] for _ in range(N)]
ALL_VISITED = (1 << N)-1

def dfs(now, visited):
    print(now, bin(visited)[2:])
    
    for x in DP:
        print(x)
    
    if DP[now][visited] != -1: return DP[now][visited]

    if visited == ALL_VISITED:
        print("여기로 진입")
        if graph[now][0] == 0: 
            print("반환",int(1e9))
            return int(1e9)
        else:
            print("반환", graph[now][0])
            return graph[now][0]

    for next in range(1,N):
        if (visited & 1 << next) != 0: continue

        if graph[now][next] == 0: continue

        next_visited = visited | 1 << next

        print(next, bin(next_visited)[2:])
        
        if DP[now][visited] == -1:
            result = dfs(next, next_visited) + graph[now][next]
            print(next,bin(next_visited)[2:],"를 넣고 ",result,"를 돌려받음")
            DP[now][visited] = result

        else: DP[now][visited] = min(DP[now][visited], dfs(next, next_visited)+graph[now][next])
        
    if DP[now][visited] == -1:
        DP[now][visited] = int(1e9)

    return DP[now][visited]

print(dfs(0, 1))