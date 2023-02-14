from collections import defaultdict
from heapq import heappop,heappush

def solution(N, road, K):
    
    INF = int(1e9)

    answer = 0
    dic = defaultdict(list)
    distance = [INF for _ in range(N+1)]
    distance[1] = 0

    for x in road:
        dic[x[0]].append([x[1],x[2]])
        dic[x[1]].append([x[0],x[2]])

    def dijkstra(distance,N):
        heap = [[1,0]]

        while heap:
            now = heappop(heap)
            for x in dic[now[0]]:

                if distance[x[0]] > now[1]+x[1]:
                    distance[x[0]]= now[1]+x[1]
                    heappush(heap,[x[0],now[1]+x[1]])

    dijkstra(distance,N)

    for x in distance[1:]:
        if x<=K:
            answer += 1

    return answer