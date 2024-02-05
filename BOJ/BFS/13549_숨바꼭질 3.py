from collections import deque, defaultdict

N, K = map(int,input().split())
MAX = 100_000

deq = deque([[N,0]])
table = defaultdict(lambda : int(1e9))

while deq:
    now, now_cost = deq.popleft()
    # print(now, now_cost)
    
    if now == K:
        print(now_cost)
        break
    
    if now*2 <= MAX:
        if table[now*2] > now_cost:
            deq.appendleft([now*2,now_cost])
            table[now*2] = now_cost

    if now-1 >= 0:
        if table[now-1] > now_cost:
            deq.append([now-1,now_cost+1])
            table[now-1] = now_cost+1

    if now+1 <= MAX:
        if table[now+1] > now_cost:
            deq.append([now+1,now_cost+1])
            table[now+1] = now_cost+1