import sys
from collections import defaultdict

def input(): return sys.stdin.readline().rstrip()

RIGHT_UP = 11
UP = 12
LEFT_UP = 13
LEFT_DOWN = 14
DOWN = 15
RIGHT_DOWN = 16

def move(now_x, now_y, direction):
    if direction == RIGHT_UP:
        return (now_x+1, now_y+1)
    elif direction == UP:
        return (now_x, now_y+2)
    elif direction == LEFT_UP:
        return (now_x-1, now_y+1)
    elif direction == LEFT_DOWN:
        return (now_x-1, now_y-1)
    elif direction == DOWN:
        return (now_x, now_y-2)
    elif direction == RIGHT_DOWN:
        return (now_x+1, now_y-1)

def find_available_resource(x, y, now_resource, board):
    dedicates = {1, 2, 3, 4, 5}
    
    if board[(y-1,x-1)] != 0:
        dedicates.discard(board[(y-1,x-1)])
        
    if board[(y-2,x)] != 0:
        dedicates.discard(board[(y-2,x)])
        
    if board[(y-1,x+1)] != 0:
        dedicates.discard(board[(y-1,x+1)])
        
    if board[(y+1,x-1)] != 0:
        dedicates.discard(board[(y+1,x-1)])
    
    if board[(y+2,x)] != 0:
        dedicates.discard(board[(y+2,x)])
        
    if board[(y+1,x+1)] != 0:
        dedicates.discard(board[(y+1,x+1)])
        
    remains = sorted(list(dedicates))
    
    _min = int(1e9)
    idx = -1
    for remain in remains:
        if _min > now_resource[remain]:
            _min = now_resource[remain]
            idx = remain
            
    return idx

C = int(input())

answer = [0 for _ in range(10001)]
now_resource = defaultdict(int) # 현재 사용되고 있는 자원의 현황판
board = defaultdict(int)

now = 1
now_x, now_y = 0,0
board[(0,0)] = 1
now_resource[1] += 1
answer[1] = 1
cycle_size = 1

while now < 10000:
    for _dir in range(11,17):
        for _ in range(cycle_size if (_dir != UP) else cycle_size-1):
            now_x, now_y = move(now_x, now_y, _dir)
            resource = find_available_resource(now_x, now_y, now_resource, board)
            now_resource[resource] += 1
            board[(now_y,now_x)] = resource
            now += 1
            answer[now] = resource
                
            if now >= 10000: break
        if now >= 10000: break
    cycle_size += 1

for _ in range(C):
    target = int(input())
    print(answer[target])

# 중앙에서부터 시작해서 나선형으로 나아감
# 각 타일은 육각형임

# 새로운 타일은 이미 채워진 인접한 타일에 들어있는 자원과 다른 자원이어야 한다.
# 가능한 자원이 여러 가지인 경우에는, 보드에 가장 적게 나타난 자원을 선택한다.
# 그러한 경우도 여러 가지라면, 번호가 작은 것을 선택한다.

# n번째에 둘 자원은 정해져있으므로 한 번만 돌리면 됨.

