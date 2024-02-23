from collections import deque

subin, baby = map(int,input().split())
temp = 0

if baby > subin:
    temp = baby - subin + baby


deq = deque()
deq.append([subin,0])

min_time = int(1e9)
count = 0
dp_table = [int(1e9) for _ in range(200_001)]
dp_table[subin] = 0

while deq:
    now_position, now_time = deq.popleft()

    if now_position == baby:
        if now_time < min_time:
            min_time = now_time
            count = 1

        elif now_time == min_time:
            count += 1

        continue

    if now_position < baby and dp_table[now_position+1] >= now_time+1:
        dp_table[now_position+1] = now_time+1
        deq.append([now_position+1,now_time+1])
        
    if now_position > 0 and dp_table[now_position-1] >= now_time+1: 
        dp_table[now_position-1] = now_time+1
        deq.append([now_position-1,now_time+1])

    if now_position*2 <= temp and dp_table[now_position*2] >= now_time+1:
        dp_table[now_position*2] = now_time+1
        deq.append([now_position*2,now_time+1])

print(min_time)
print(count)