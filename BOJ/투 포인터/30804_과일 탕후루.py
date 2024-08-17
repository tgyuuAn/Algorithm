from collections import defaultdict, deque
import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
fruits = list(input().split())

deq = deque()
counter = defaultdict(int)
start = 0
end = 0
max_fruits = 0
while start <= N-1:
    if start == end: 
        end += 1
        deq.append(fruits[start])
        counter[fruits[start]] += 1

    elif len(counter) > 2:
        start += 1
        popped_fruit = deq.popleft()
        counter[popped_fruit] -= 1
        if counter[popped_fruit] == 0: del counter[popped_fruit]

    else:
        if end == N: break
        end += 1
        deq.append(fruits[end-1])
        counter[fruits[end-1]] += 1
    
    if len(counter) <= 2 and max_fruits < len(deq):
        max_fruits = len(deq)
        
print(max_fruits)