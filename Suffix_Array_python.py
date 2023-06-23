def solution(my_string):
    answer = []
    for x in range(1,len(my_string)+1):
        answer.append(my_string[-1*x:])
    return sorted(answer)