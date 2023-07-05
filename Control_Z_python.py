def solution(s):
    answer = 0
    s=s.split()
    while "Z" in s:
        temp = s.index("Z")
        s.pop(temp)
        s.pop(temp-1)
        
    for x in s:
        answer += int(x)
    return answer