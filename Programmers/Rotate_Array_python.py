def solution(numbers, direction):
    answer = []
    if direction == "right":
        answer.append(numbers.pop())
        for number in numbers:
            answer.append(number)
    else:
        numbers.append(numbers.pop(0))
        for number in numbers:
            answer.append(number)
    return answer