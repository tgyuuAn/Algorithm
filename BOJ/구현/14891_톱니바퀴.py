import sys

def input(): return sys.stdin.readline().rstrip()
gears = [input() for _ in range(4)]

def rotate_gear(now_number, dir, visited):
    visited.add(now_number)
    
    origin = gears[now_number][:]
    
    if(dir == 1): gears[now_number] = gears[now_number][-1] + gears[now_number][0:-1]
    elif(dir == 0): return
    else: gears[now_number] = gears[now_number][1] + gears[now_number][2:] + gears[now_number][0]
    
    left_gear = now_number - 1
    if left_gear >= 0 and left_gear not in visited:
        left_dir = 0 if(origin[6] == gears[left_gear][2]) else dir * -1
        rotate_gear(left_gear, left_dir, visited)
    
    right_gear = now_number + 1
    if right_gear <= 3 and right_gear not in visited:
        right_dir = 0 if(origin[2] == gears[right_gear][6]) else dir * -1
        rotate_gear(right_gear, right_dir, visited)
 
    return

K = int(input())
for _ in range(K):
    gear_number, dir = map(int, input().split())
    rotate_gear(gear_number-1, dir, set())

answer = 0
for idx in range(4): 
    if gears[idx][0] == "1": answer += 2**(idx)
    
print(answer)