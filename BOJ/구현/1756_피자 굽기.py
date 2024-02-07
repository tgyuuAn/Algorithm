from collections import deque

oven_depth_count, pizza_dough_count = map(int,input().split())

oven_depth = list(map(int,input().split()))
pizza_dough = deque(map(int,input().split()))

max_diameter = int(1e9)
for idx, oven in enumerate(oven_depth):
    max_diameter = min(max_diameter, oven)
    oven_depth[idx] = max_diameter

for idx, oven in enumerate(oven_depth[::-1]):
    if pizza_dough[0] <= oven: pizza_dough.popleft()

    if len(pizza_dough) == 0: 
        print(len(oven_depth)-idx)
        break

if len(pizza_dough) > 0: print(0)