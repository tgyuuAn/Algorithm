from collections import deque

def solution(queue1, queue2):
    
    queue1, queue2 = deque(queue1), deque(queue2)
    answer = 0
    
    tot1,tot2= sum(queue1), sum(queue2)
    target = (tot1+tot2)// 2
    n = len(queue1)
    
    while tot1 != tot2:

        if answer >= n*2+1:
            answer = -1
            break

        if tot1 > tot2:
            temp = queue1.popleft()
            queue2.append(temp)
            tot1 -= temp
            tot2 += temp
            answer +=1

        else:
            temp = queue2.popleft()
            queue1.append(temp)
            tot1 += temp
            tot2 -= temp
            answer+=1

    return answer
