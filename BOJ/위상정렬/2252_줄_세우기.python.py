from collections import deque

total_student_number, total_compare_count = map(int,input().split(" "))

highers = [[] for _ in range(total_student_number+1)]
indegrees = [0 for _ in range(total_student_number+1)]

for _ in range(total_compare_count):
    lower, higher = map(int, input().split(" "))
    highers[lower].append(higher)
    indegrees[higher] += 1

deq = deque([])

for idx, indegree in enumerate(indegrees):
    if indegree == 0 and idx != 0:
        deq.append(idx)

while deq:
    now = deq.popleft()
    print(now, end=" ")

    for higher in highers[now]:
        indegrees[higher] -= 1

        if indegrees[higher] == 0:
            deq.append(higher)