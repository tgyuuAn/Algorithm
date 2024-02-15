from collections import deque

total_blog_day, duration = map(int,input().split())

_max = 0
max_duration = 0
deq = deque()
now = 0
for today in map(int,input().split()):
    if len(deq) >= duration:
        top = deq.popleft()
        now -= top
        deq.append(today)
        now += today

    elif len(deq) < duration:
        now += today
        deq.append(today)

    if _max < now:
        _max = now
        max_duration = 1

    elif _max == now:
        max_duration += 1

if _max == 0: print("SAD")
else:
    print(_max)
    print(max_duration)