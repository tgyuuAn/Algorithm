import sys
from collections import deque

total_test_case = int(sys.stdin.readline())
for _ in range(total_test_case):
    house_count, steal_count, maximum = map(int,sys.stdin.readline().split())
    house_information = list(sys.stdin.readline().split())
    house_information.extend(house_information[:steal_count])

    answer = 0
    accumulate = 0
    window = deque()
    for idx in range(house_information):
        if len(window) < steal_count:
            window.append(house_information[idx])
            accumulate += house_information[idx]

        else:
            accumulate -= house_information.popleft()
            window.append(house_information[idx])
            accumulate += house_information[idx]

        if accumulate < maximum: answer += 1

    print(answer)