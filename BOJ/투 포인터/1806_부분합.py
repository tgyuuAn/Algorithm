import sys

N, S = map(int,sys.stdin.readline().split())
numbers = list(map(int,sys.stdin.readline().split()))

start = 0
end = 0
accumulate = numbers[0]
answer = int(1e9)
while start <= end:
    if accumulate >= S:
        answer = min(answer, end-start+1)
        
        accumulate -= numbers[start]
        start+=1

    elif accumulate < S:
        if end == N-1: break
        else:
            end+=1
            accumulate += numbers[end]

if answer == int(1e9): print(0)
else: print(answer)