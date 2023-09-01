def solution(my_string):
    answer = []
    for x in range(52):
        answer.append(0)

    for word in my_string:
        if ord(word)>=65 and ord(word)<=90:
            answer[ord(word)-65]+=1
        
        if ord(word)>=97 and ord(word)<=122:
            answer[ord(word)-71]+=1
        
    return answer