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

    print(outdegree)

    for root in range(1,sequence_size+1):
        if visited[root] == True:
            continue

        deq = deque([root])
        root_table[root] = root
        visited[root] = True
        print()
        print(root, root_table)
        
        while deq:
            now = deq.popleft()
            next = outdegree[now]
            print("deq : ",deq)
            print("now : ",now)
            print("next : ",next)
            print("visited : ",visited)
            print("root_table : ",root_table)
            
            if visited[next] == True and root_table[next] == root:
                print("빠짐")
                answer += 1
                break

            if visited[next] == True:
                continue
            
            deq.append(next)
            visited[next] = True
            root_table[next] = root

    print(answer)