import sys
from collections import deque

string = list(sys.stdin.readline().rstrip())

a_indexes = deque()
b_indexes = deque()
c_indexes = deque()
answer = 0

for idx, char in enumerate(string):
    if char == "A": a_indexes.append(idx)

    elif char == "B": b_indexes.append(idx)

    elif char == "C": c_indexes.append(idx)

while b_indexes and c_indexes:
    b_now = b_indexes[0]

    while c_indexes:
        c_now = c_indexes.popleft()

        if b_now < c_now:
            b_indexes.popleft()
            answer += 1
            break

while a_indexes and b_indexes:
    a_now = a_indexes.popleft()

    while b_indexes:
        b_now = b_indexes.popleft()

        if a_now < b_now:
            answer += 1
            break

print(answer)