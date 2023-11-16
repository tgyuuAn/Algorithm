from collections import deque

def solution(people, limit):
    people = deque(sorted(people))
    count = 0

    while people:
        tempNow = people.pop()

        while people:
            if tempNow + people[0] <= limit:
                tempNow += people.popleft()
            else:
                break
        count += 1

    return count
