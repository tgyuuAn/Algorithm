from collections import deque
import sys

def input(): return sys.stdin.readline().rstrip()
N, K = map(int, input().split())

parent = [-1 for _ in range(100001)]
visited = set()

deq = deque([[N, 0]])
while deq:
    now, now_count = deq.popleft()

    if now == K:
        print(now_count)

        if N == K:
            print(N)
            break
        
        answer = deque([now])
        prev = parent[now]
        while prev != N:
            answer.appendleft(prev)
            prev = parent[prev]

        answer.appendleft(N)
        
        print(*answer)
        break

    if now != 0 and now*2 <= 100000 and now*2 not in visited:
        visited.add(now*2)
        parent[now*2] = now
        deq.append([now*2, now_count+1])
        
    if now-1 >= 0 and now-1 not in visited:
        visited.add(now-1)
        parent[now-1] = now
        deq.append([now-1, now_count+1])
        
    if now < K and now+1 not in visited:
        visited.add(now+1)
        parent[now+1] = now
        deq.append([now+1, now_count+1])
        