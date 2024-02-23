from heapq import *

N, M, L = map(int,input().split())

rest_areas = [0]
rest_areas.extend(list(int,input().split()))
rest_areas.sort()
rest_areas.append(M)
heap = []

for idx in range(1,len(rest_areas)):
    heappush(heap, -1 * (rest_areas[idx] - rest_areas[idx-1]))

answer = int(1e9)

def dfs(heap, remain_count):
    global answer

    if remain_count == 0:
        answer = min(answer, -1*heappop(heap))
        return
           
    now = heappop(heap)
    now_heap = heap[:]

    for count in (remain_count+1,1,-1):
        for _ in range(count):
            heappush(now_heap,now//count)

        dfs(now_heap, remain_count-count)

dfs(heap, M)
print(answer)