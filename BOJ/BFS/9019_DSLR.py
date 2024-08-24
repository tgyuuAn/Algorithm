from collections import deque
import sys

def input(): return sys.stdin.readline().rstrip()
for _ in range(int(input())):
    A, B = map(int, input().split())

    deq = deque()
    visited = {A,}
    deq.append((A, ""))
    while deq:
        now_value, history = deq.popleft()

        if now_value == B:
            print(history)
            break

        for query in range(4):
            if query == 0:
                new_value = int(now_value*2%10000)
            
                if new_value in visited: continue
        
                new_history = history+"D"
                
            elif query == 1:
                new_value = now_value-1 if now_value != 0 else 9999

                if new_value in visited: continue
                
                new_history = history+"S"
    
            elif query == 2:
                str_now_value = str(now_value)
                while len(str_now_value) < 4:
                    str_now_value = "0" + str_now_value
                
                new_value = int(str_now_value[1]+str_now_value[2]+str_now_value[3]+str_now_value[0])
    
                if new_value in visited: continue
                
                new_history = history+"L"
    
            else:
                str_now_value = str(now_value)
                while len(str_now_value) < 4:
                    str_now_value = "0" + str_now_value
                new_value = int(str_now_value[3]+str_now_value[0]+str_now_value[1]+str_now_value[2])

                if new_value in visited: continue

                new_history = history+"R"
        
            visited.add(new_value)
            deq.append((new_value, new_history))