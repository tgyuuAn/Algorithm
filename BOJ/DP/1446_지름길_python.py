from collections import defaultdict, deque

shortcut_count, road_length = map(int,input().split())
graph = defaultdict(lambda : int(1e9))

for _ in range(shortcut_count):
    start, destination, cost = map(int,input().split())
    if destination > road_length:
        continue

    graph[(start,destination)] = min(graph[(start,destination)],cost)

#시작 지점을 기준으로 정렬
graph = deque(sorted(list(graph.items()), key=lambda x:x[0][0]))
dp_table = defaultdict(lambda : int(1e9))
dp_table[0] = 0

while graph:
    now_information, now_cost = graph.popleft()
    now_start, now_destination = now_information

    for key in list(dp_table.keys())[:]:
        if now_start < key:
            dp_table[now_destination] = min(dp_table[now_destination], now_start + now_cost)
            continue

        dp_table[now_destination] = min(dp_table[now_destination], dp_table[key] + (now_start - key) + now_cost)

for key in list(dp_table.keys())[:]:
    dp_table[road_length] = min(dp_table[road_length], dp_table[key] + (road_length - key))

print(dp_table[road_length])