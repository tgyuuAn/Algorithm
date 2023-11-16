from itertools import permutations

def solution(babbling):
    speak = ["aya", "ye", "woo", "ma"]
    answer = 0
    can_speak = []
    
    for x in range(1,5):
        for word_list in permutations(speak,x):
            temp = ""
            for word in word_list:
                temp+=word
            can_speak.append(temp)
             
    for bab in babbling:
        if bab in can_speak:
            answer += 1
    return answer