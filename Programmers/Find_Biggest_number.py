from collections import deque

def solution(number, k):
    number = deque(number)
    temp = deque()
    temp.append(number.popleft())
    for i in number:
        while temp[-1]<i and k!=0:
            temp.pop()
            k-=1
            if not temp:
                break
        temp.append(i)
    return "".join(temp) if k==0 else "".join(temp)[:-k]

print(solution("1924",2))