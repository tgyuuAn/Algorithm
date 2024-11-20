from collections import defaultdict
import sys

def input(): return sys.stdin.readline().rstrip()

N, H = map(int, input().split())

floors = []
bottoms = []
for idx in range(N):
    height = int(input())
    height *= -1
        
    if idx%2==0: floors.append(height)
        
    else: bottoms.append(height)

floors.sort()
bottoms.sort()

f_prefix_sum = defaultdict(int)
p_f_h = 0
for f_h in floors:
    if p_f_h == 0 or p_f_h == f_h:
        f_prefix_sum[f_h] += 1
    else:
        f_prefix_sum[f_h] = f_prefix_sum[p_f_h] + 1
        
    p_f_h = f_h

b_prefix_sum = defaultdict(int)
p_b_h = 0
for b_h in bottoms:
    if p_b_h == 0 or p_b_h == b_h:
        b_prefix_sum[b_h] += 1
    else:
        b_prefix_sum[b_h] = b_prefix_sum[p_b_h] + 1
    
    p_b_h = b_h

b_temp = []
for b_h in range(H, 0, -1):
    if -1*b_h in b_prefix_sum: b_temp.append(b_prefix_sum[-1*b_h])
    else: 
        if b_temp: b_temp.append(b_temp[-1])
        else: b_temp.append(0)
b_temp.reverse()        

f_temp = []
for f_h in range(H, 0, -1):
    if -1*f_h in f_prefix_sum: f_temp.append(f_prefix_sum[-1*f_h])
    else: 
        if f_temp: f_temp.append(f_temp[-1])
        else: f_temp.append(0)

answer = 0
min_count = int(1e9)
for idx, (b, f) in enumerate(zip(b_temp, f_temp)):
    temp = b+f
    if min_count > temp:
        answer = 1
        min_count = temp
    elif min_count == temp:
        answer += 1

print(f"{min_count} {answer}")