import sys
from itertools import combinations

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
chicken = []
house = []
for row in range(N):
    _input = list(input().split())
    
    for col, element in enumerate(_input):
        if element == "1": house.append((len(house),row, col))
        elif element == "2": chicken.append((len(chicken),row, col))
        
board = [[0 for _ in range(len(chicken))] for _ in range(len(house))]

for house_idx, house_row, house_col in house:
    for chicken_idx, chicken_row, chicken_col in chicken:
        gap = abs((chicken_row - house_row)) + abs((chicken_col - house_col))
        board[house_idx][chicken_idx] = gap

answer = int(1e9)
for chickens in combinations(range(len(chicken)), M):
    temp = 0
    
    for house in board:
        min_value = int(1e9)
        
        for chicken_idx in chickens:
            min_value = min(min_value, house[chicken_idx])
    
        temp += min_value
    
    answer = min(answer, temp)
    
print(answer)