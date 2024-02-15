from collections import defaultdict

total_test_case = int(input())

answer = False

def dfs(a_set, b_set, graph_information, start_idx):
    global answer

    if start_idx == len(graph_information):
        return True
        pass

    for idx, vertex in enumerate(graph_information[start_idx:]):
        if vertex in a_set: continue

        a_set.add(vertex)
        
        for neighbor_vertex in graph_information[vertex]:
            if neighbor_vertex in a_set: break
            
            b_set.add(neighbor_vertex)

        else: dfs(a_set, b_set, graph_information, start_idx+idx+1)

        a_set.discard(vertex)

        for neighbor_vertex in graph_information[vertex]:
            b_set.discard(neighbor_vertex)

for _ in range(total_test_case):
    vertex_count, edge_count = map(int,input().split())

    graph_information = defaultdict(list)

    for _ in edge_count:
        start, destination = map(int,input().split())
        graph_information[start].append(destination)
        graph_information[destination].append(start)

    a_set, b_set = set(), set()

    dfs(a_set, b_set, graph_information, 0)

    print(graph_information)
    print(answer)