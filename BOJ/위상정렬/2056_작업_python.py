from collections import deque

length_task = int(input())
task_time = [-1]
task_indegree = [-1]
task_flow = [[] for _ in range(length_task+1)]

for task in range(1,length_task+1):
    task_information = list(map(int, input().split(" ")))
    task_time.append(task_information[0])
    task_indegree.append(task_information[1])

    if len(task_information) >= 2:
        for before_task in task_information[2:]:
            task_flow[before_task].append(task)

print(task_indegree)
print(task_time)
print(task_flow)
deq = deque([])
dp_table = [int(-1) for _ in range(length_task+1)]
for idx, indegree in enumerate(task_indegree):
        if indegree == 0:
             deq.append(idx)
             dp_table[idx] = task_time[idx]

while deq:
    now = deq.popleft()
    childs = task_flow[now]

    for child in childs:
         task_indegree[child] -= 1
         dp_table[child] = max(dp_table[child], dp_table[now]+task_time[child])
         if task_indegree[child] == 0:
              deq.append(child)

print(max(dp_table))