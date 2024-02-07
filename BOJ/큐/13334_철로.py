from collections import defaultdict, deque

total_humans_count = int(input())
road = list()

for idx in range(total_humans_count):
    house, office = map(int,input().split())
    road.extend([(house, idx),(office, idx)])

railway = int(input())

road.sort(reverse=True)

deq = deque()
board = defaultdict(int)
answer = 0
temp = 0

while road:
    now_point, idx = road.pop()

    deq.append((now_point,idx))
    board[idx] += 1
    if board[idx] == 2: temp += 1
    
    while True:
        if deq[-1][0] - deq[0][0] > railway:
            deq.popleft()
            board[deq[0][1]]-=1
            
            if board[deq[0][1]] == 1: temp -= 1

        else: break

    answer = max(answer,temp)

print(answer)
    