from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    
    while goal:
        target = goal[0]
        
        if cards1 and cards1[0] == target:
            cards1.popleft()
            goal.popleft()
            
        elif cards2 and cards2[0] == target:
            cards2.popleft()
            goal.popleft()
            
        else:
            return "No"

    return "Yes"