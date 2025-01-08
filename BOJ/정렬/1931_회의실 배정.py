import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
meetings = []
for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))
    
meetings.sort(reverse = True)
answer = 0
now = []
while meetings:
    now_start, now_end = meetings.pop()
    
    while now and now[-1][1] > now_end:
        now.pop()
    
    if not now or (now and now_start >= now[-1][1]):
        now.append((now_start, now_end))
        
    answer = max(answer, len(now))

print(answer)