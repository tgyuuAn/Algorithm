import sys

def input(): return sys.stdin.readline()

N = int(input())
xy = []
center_x = 0
center_y = 0
for _ in range(N):
    x, y = map(int,input().split())
    center_x += x
    center_y += y
    xy.append([x,y])

center_x /= N
center_y /= N
xy.append(xy[0])
print(center_x)
print(center_y)

def get_triangle_wide(x1, y1, x2, y2, x3, y3):
    A = (x1*y2 + x2*y3 + x3*y1)
    B = (x2*y1 + x3*y2 + x1*y3)
    return (A - B)

answer = 0
for prev_idx in range(N):
    prev_x, prev_y = xy[prev_idx][0], xy[prev_idx][1]
    next_x, next_y = xy[prev_idx+1][0], xy[prev_idx+1][1]

    answer += get_triangle_wide(center_x, center_y, prev_x, prev_y, next_x, next_y)
    
answer = abs(answer)
answer *= 0.5
print(round(answer,1))