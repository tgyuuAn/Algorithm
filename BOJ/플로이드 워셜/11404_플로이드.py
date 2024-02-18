import sys

city_count = int(sys.stdin.readline())
bus_count = int(sys.stdin.readline())

cost_table = [[int(1e9) for _ in range(city_count+1)] for _ in range(city_count+1)]

for idx in range(1,city_count+1):
    cost_table[idx][idx] = 0

for _ in range(bus_count):
    start, destination, cost = map(int,sys.stdin.readline().split())
    cost_table[start][destination] = min(cost_table[start][destination], cost)

for mid in range(1,city_count+1):
    for start in range(1, city_count+1):
        for destination in range(1, city_count+1):
            cost_table[start][destination] = min(cost_table[start][destination], cost_table[start][mid] + cost_table[mid][destination])

for cost in cost_table[1:]:
    print(*map(lambda x : 0 if(x==int(1e9)) else x,cost[1:]))