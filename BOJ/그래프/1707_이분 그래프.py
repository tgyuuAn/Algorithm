from collections import defaultdict, deque
import sys

total_test_case = int(sys.stdin.readline())
A = 0
B = 1

for _ in range(total_test_case):
    vertex_count, edge_count = map(int,sys.stdin.readline().split())
    graph_information = defaultdict(set)
    answer = True

    for _ in range(edge_count):
        start, destination = map(int,sys.stdin.readline().split())
        graph_information[start].add(destination)
        graph_information[destination].add(start)

    a_set, b_set = set(), set()
    for vertex in graph_information:
        if vertex in a_set or vertex in b_set: continue

        deq = deque()

        if len(a_set) == 0 and len(b_set) == 0:
            deq.append([vertex, A])
            a_set.add(vertex)

        if len(graph_information[vertex] - a_set) == len(graph_information[vertex]):
            deq.append([vertex, A])
            a_set.add(vertex)
 
        elif len(graph_information[vertex] - b_set) == len(graph_information[vertex]):
            deq.append([vertex, B])
            a_set.add(vertex)

        while deq:
            now, flag = deq.popleft()

            for neighbor_vertex in graph_information[now]:
                if flag == A and neighbor_vertex in b_set: continue
                if flag == B and neighbor_vertex in a_set: continue
                if flag == A and neighbor_vertex in a_set: 
                    answer = False
                    break

                if flag == B and neighbor_vertex in b_set: 
                    answer = False
                    break
                
                if flag == A:
                    b_set.add(neighbor_vertex)
                    deq.append([neighbor_vertex, B])

                elif flag == B:
                    a_set.add(neighbor_vertex)
                    deq.append([neighbor_vertex, A])

        if answer == False: break
    if answer: print("YES")
    else: print("NO")