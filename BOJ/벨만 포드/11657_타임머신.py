import sys

city_count, bus_count = map(int,sys.stdin.readline().split())
city_table = [int(1e9) for _ in range(city_count+1)]
city_table[1] = 0
bus_information = []

for _ in range(bus_count):
    bus_information.append(list(map(int,sys.stdin.readline().split())))
    
cycle_flag = False
for i in range(city_count):
    for start, destination, cost in bus_information:
        if city_table[start] != int(1e9) and city_table[destination] > city_table[start] + cost:
            city_table[destination] = city_table[start] + cost

            if i == city_count-1:
                cycle_flag = True

if cycle_flag: print(-1)
else:
    for cost in city_table[2:]:
        if cost == int(1e9): print(-1)
        else: print(cost)   