from collections import deque

total_number_count, gap = map(int,input().split(" "))

numbers = list(map(int, input().split(" ")))

buffer = deque([])
for idx, number in enumerate(numbers):

    while buffer and buffer[-1][0] > number:
        buffer.pop()           

    buffer.append([number,idx])

    if buffer[0][1] <= idx - gap:
        buffer.popleft()

    print(buffer[0][0], end=" ")