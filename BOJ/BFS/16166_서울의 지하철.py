from collections import defaultdict, deque
import sys

def input(): return sys.stdin.readline().rstrip()

line_graph = defaultdict(list)
link_graph = defaultdict(list)

start_lines = list()
destination_line = -1
N = int(input())

for line in range(N):
    line_info = list(map(int, input().split()))[1:]

    for line_number in line_info:
        if line_number == 0: start_lines.append(line)

        link_graph[line_number].append(line)
        
    line_graph[line].extend(line_info)

destination_line_number = int(input())

for line, line_info in line_graph.items():

    for line_number in line_info:
        if line_number == destination_line_number: 
            destination_line = line
            break
        
    if destination_line != -1: break

if destination_line != -1:
    answer = int(1e9)
    
    for start_line in start_lines:
        visited = {start_line,}
        deq = deque([(0, start_line)])
        while deq:
            now_count, now_line = deq.popleft()
        
            if now_line == destination_line:
                answer = min(answer, now_count)
                break
        
            for line_number in line_graph[now_line]:
                for linked_line in link_graph[line_number]:
                    if linked_line in visited: continue
        
                    visited.add(linked_line)
                    deq.append((now_count+1, linked_line))
    
    print(answer) if answer != int(1e9) else print(-1)                
else: print(-1)