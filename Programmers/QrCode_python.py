def solution(q, r, code):
    answer = ""
    for index,x in enumerate(code):
        if index%q==r:
            answer += x
    return answer