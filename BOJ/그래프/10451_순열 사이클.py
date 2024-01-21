# DFS-BFS를 이용한 풀이
from collections import defaultdict, deque

total_case = int(input())

for _ in range(total_case):
    sequence_size = int(input())
    sequence = [None]
    sequence.extend(map(int,input().split()))

    root_table = [None for _ in range(sequence_size+1)]
    outdegree = defaultdict(int)
    for start, destination in enumerate(sequence):
        outdegree[start] = destination

    visited = [False for _ in range(sequence_size+1)]
    visited[0] = True

    answer = 0
    for root in range(1,sequence_size+1):
        if visited[root] == True:
            continue

        deq = deque([root])
        root_table[root] = root
        visited[root] = True

        while deq:
            now = deq.popleft()
            next = outdegree[now]
            
            if visited[next] == True and root_table[next] == root:
                answer += 1
                break

            if visited[next] == True:
                continue
            
            deq.append(next)
            visited[next] = True
            root_table[next] = root

    print(answer)


## 유니온 파인드를 이용한 풀이
from collections import defaultdict

total_case = int(input())

def find_parent(child,info):
    if info[child] == child: return info[child]
    else: info[child] = find_parent(info[child], info)
    return info[child]
    
def union_parent(a,b,info):
    a = find_parent(a, info)
    b = find_parent(b, info)
    if a<b: info[b] = a
    else: info[a] = b

for _ in range(total_case):
    sequence_size = int(input())
    sequence = [None]
    sequence.extend(map(int,input().split()))
 
    outdegree = [x for x in range(sequence_size+1)]
    answer = 0
    for start, destination in enumerate(sequence):
        if start == 0:
            continue

        if find_parent(start, outdegree) == find_parent(destination, outdegree): answer += 1
        else: union_parent(start,destination,outdegree)
        
    print(answer)