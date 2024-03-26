import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())

def dfs(target, visited, now, now_set):
    answer = 0

    if target == now:
        print(now_set)
        visited.add(now_set)
        return 1

    for num in [1,2,3]:
        if now - num <= target:
            now_set.add(num)
            answer += dfs(target, visited, now+num)
            now_set.discard(num)

    return answer

for _ in range(N):
    target = int(input())
    visited = set()
    now_set = set()
    print(dfs(target, visited, 0, now_set))