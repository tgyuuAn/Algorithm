def solution(chicken):
    answer = 0
    while chicken>=10:
        temp, mod = divmod(chicken,10)
        answer += temp
        chicken = temp+mod
        
    return answer5