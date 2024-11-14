from itertools import combinations
import sys

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
hospital = []
people = []
for row in range(N):
    _input = list(map(int, input().split()))
    for col in range(N):
        if _input[col] == 1:
            people.append((row, col))
        elif _input[col] == 2:
            hospital.append((row, col))      

answer = int(1e9)
for items in combinations(hospital, M):
    dedicate = 0
    for person in people:        
        _min = int(1e9)

        for item in items:
            temp = abs(item[0] - person[0]) + abs(item[1] - person[1])
            _min = min(_min, temp)

        dedicate += _min
    answer = min(answer, dedicate)

print(answer)
    