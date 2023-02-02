def solution(s):
    n = len(s)
    answer = 0

    for x in range(n):
        temp = []
        for y in range(x,x+n):
            z = y%n
            word = s[z]
            temp.append(word)
            
            if len(temp) >= 2:
                if (temp[-2] == "(" and temp[-1] == ")") or (temp[-2] == "[" and temp[-1] == "]") or (temp[-2] == "{" and temp[-1] == "}"):
                    temp.pop()
                    temp.pop()
        
        if len(temp) == 0:
            answer += 1
    return answer


s="[](){}"
solution(s)