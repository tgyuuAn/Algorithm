import sys
from itertools import combinations

N = int(sys.stdin.readline())
solution = list(map(int,sys.stdin.readline().split()))
solution.sort()

answer = int(1e9)

def check(x, y, mid):
    if solution[x] + solution[y] + solution[mid] > 0: return True
    return False

min_value = int(1e10)
answer = []
for x in range(N-2):
    for y in range(x+1,N-1):
        left = y
        right = N
        while left+1<right:
            mid = (left+right)//2

            if check(x,y,mid): right = mid
            else: left = mid

        if left > y and abs(solution[x] + solution[y] + solution[left]) < min_value:
            min_value = abs(solution[x] + solution[y] + solution[left])
            answer = [solution[x], solution[y], solution[left]]

        if right < N and abs(solution[x] + solution[y] + solution[right]) < min_value:
            min_value = abs(solution[x] + solution[y] + solution[right])
            answer = [solution[x], solution[y], solution[right]]

print(*answer)