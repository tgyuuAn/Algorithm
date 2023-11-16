def solution(numbers):
    answer = [-1 for _ in numbers]
    temp = []

    for idx, i in enumerate(range(len(numbers))):
        now = numbers[i]

        while temp:
            if temp[-1][1] < now:
                temp2 = temp.pop()
                answer[temp2[0]] = now
            else:
                break

        temp.append([idx,now])
        
    return answer
