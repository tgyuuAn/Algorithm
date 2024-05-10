import sys

def input(): return sys.stdin.readline().rstrip()

INF = int(1e9)
N = int(input())
M = int(input())
not_working_buttons = set(input().split())
working_buttons = set(str(x) for x in range(10))
working_buttons -= not_working_buttons
min_gap = max(100 - N, N - 100)
answer = min_gap

def dfs(num, depth, working_buttons):
    global answer, min_gap
    
    if len(str(N))-1 <= depth and depth <= len(str(N))+1:
        gap = max(int(num) - N, N - int(num))
        if min_gap >= gap:
            answer = min(answer,(depth + gap))
            min_gap = gap
            
    if depth == len(str(N))+1: return

    for button in working_buttons:
        dfs(num+button, depth+1, working_buttons)

min_gap = max(100 - N, N - 100)
for button in working_buttons:
    if button == "0":
        gap = N
        if min_gap > gap:
            answer = N+1
            min_gap = N
        continue
    
    dfs(button, 1, working_buttons)

print(answer)