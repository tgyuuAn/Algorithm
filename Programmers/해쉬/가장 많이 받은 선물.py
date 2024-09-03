from collections import defaultdict
from itertools import *

def solution(friends, gifts):
    answer = 0
    send_gift_score = defaultdict(int)
    receive_gift_score = defaultdict(int)
    
    for gift in gifts:
        _from, _to = gift.split()
        send_gift_score[gift] += 1
        send_gift_score[_from] += 1
        receive_gift_score[_to] += 1
    
    answer = defaultdict(int)
    for x, y in combinations(friends, 2):
        x_y = send_gift_score[f"{x} {y}"]
        y_x = send_gift_score[f"{y} {x}"]
        
        if x_y > y_x:
            answer[x] += 1
        elif y_x > x_y:
            answer[y] += 1
        else:
            x_score = send_gift_score[x] - receive_gift_score[x]
            y_score = send_gift_score[y] - receive_gift_score[y]
            
            if x_score > y_score:
                answer[x] += 1
            elif y_score > x_score:
                answer[y] += 1
    
    return max(answer.values()) if answer else 0