def solution(my_string, m, c):
    answer = ""
    count = 0
    temp = ""
    for word in my_string:
        if count < m:
            temp += word
            count += 1
        if count == m:
            count = 0
            answer += temp[c-1]
            temp = ""
    return answer