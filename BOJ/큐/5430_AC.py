from collections import deque
import sys

def input(): return sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    queries = deque(input())
    n = int(input())

    numbers = deque(input().strip("[").strip("]").replace(",", " ").split())
    
    reverse = False
    while queries:
        now_query = queries.popleft()
        
        if now_query == "R": reverse = not reverse
        
        elif now_query == "D" and len(numbers) >= 1:
            if reverse: numbers.pop()
            else: numbers.popleft()
        
        else:
            print("error", end="")
            break

    else:
        print("[", end="")
        if reverse: print(",".join(reversed(numbers)), end="")
        else: print(",".join(numbers), end="")
        print("]", end="")
        
    print()