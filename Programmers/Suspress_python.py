from collections import defaultdict,deque

def solution(msg):
    answer = []
    dic = defaultdict(int)
    for index, word in enumerate(range(65,91)):
        dic[chr(word)] = index+1
    
    msg = deque(msg)
    index= 27
    while msg:
        temp = ""
        while msg:
            x=msg[0]
            if temp+x in dic:
                msg.popleft()
                temp = temp+x
            else:
                break
        
        answer.append(dic[temp])
        if msg:
            temp = temp+msg[0]

        dic[temp] = index
        index += 1
    return answer

msg = "KAKAO"
solution(msg)