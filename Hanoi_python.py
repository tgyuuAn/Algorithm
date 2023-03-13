answer = []

def hanoi(n,now,target,sub):
    global answer
    
    if n==1:
        answer.append([now,target])
    
    else:
        hanoi(n-1,now,sub,target)
        answer.append([now,target])
        hanoi(n-1,sub,target,now)
    

def solution(n):
    global answer
    hanoi(n,1,3,2)
    return answer