from heapq import *

sensor_count = int(input())
concentrate_count = int(input())

if sensor_count <= concentrate_count :
    print(0)

else:
    sensor_set = sorted(set(map(int,input().split())))
    gap_table = []
    
    total_distance = sensor_set[-1] - sensor_set[0]
    for idx in range(1,len(sensor_set)):
        heappush(gap_table,(-(sensor_set[idx]-sensor_set[idx-1])))
    
    print(sensor_set)
    print(gap_table)
    print(total_distance)
    
    for _ in range(concentrate_count-1):
        distance = heappop(gap_table)
        total_distance += distance
    
    print(gap_table)
    print(total_distance)