from collections import defaultdict
import heapq

def solution(targets):
    answer = 0
    dic = defaultdict(int)
    heapq.heapify(targets)
    temp_end = int(1e9)
    temp = []
    
    while targets:
        now = heapq.heappop(targets)
        
        #만약 temp리스트가 비었을 경우,
        if not temp:
            temp.append(now)
            temp_end = now[1]
        
        #비어 있지 않으면 해당 분기로 들어옴
        else:
            
            #만약 이전 타겟들의 끝 좌표(가장 가까운)가 현재 타겟의 시작 좌표보다 클 경우
            if temp_end > now[0]:
                temp.append(now)
                #현재 타겟들의 끝 좌표를 갱신한다
                temp_end = min(temp_end,now[1])
            
            #만약 이전 타겟의 끝 좌표가 현재 타겟의 시작 좌표보다 작을 경우
            else:
                temp.clear()
                answer += 1
                temp.append(now)
                temp_end = now[1]

    if temp:
        answer += 1
    return answer