from collections import defaultdict, deque

def solution(edges):
    answer = [0,0,0,0]
    out_info = defaultdict(list)
    in_info = defaultdict(list)
    nodes = set()
    
    for start, destination in edges:
        out_info[start].append(destination)
        in_info[destination].append(start)
        nodes.update((start, destination))
        
    print("나가는 정보 : ",out_info)
    print("들어오는 정보 : ",in_info)
    
    start = 0
    start_dedications = []
    for key in nodes:
        if key not in in_info.keys():
            start_dedications.append(key)
    
    print("시작 지점 후보자:",start_dedications)
    
    rod_graph_start_points = []
    if len(start_dedications) == 1:
        start = start_dedications[0]
    
    else:
        for dedication in start_dedications:
            if len(out_info[dedication]) == 1:
                rod_graph_start_points.append(dedication)
                
            else:
                start = dedication
    
    print("시작 지점:",start)
    answer[0] = start
    print("막대 모양 그래프 시작 지점:",rod_graph_start_points)
    answer[2] = len(rod_graph_start_points)
    
    # 먼저 막대 모양 그래프 시작 지점이 있을 경우, 막대 모양 그래프 부터 방문 처리 함.
    for rod_graph_start_point in rod_graph_start_points:
        
        deq = deque([rod_graph_start_point])
        while deq:
            now = deq.popleft()
            nodes.remove(now)
            deq.extend(out_info[now])
    
    for else_graph_start_point in out_info[start]:
        
        prev = else_graph_start_point
        deq = deque([else_graph_start_point])
        temp = 0
        while deq:
            now = deq.popleft()
            nodes.discard(now)
            
            # 8자 모양 그래프의 중앙 지점을 만났을 경우 탈출
            if len(out_info[now]) == 2:
                answer[3] += 1
                break
                
            # 정점과 다음 정점이 같을 경우 도넛 모양 그래프
            if len(out_info[now]) == 1 and prev == out_info[now][0]:
                answer[1] += 1
                break
                
            if len(out_info[now]) == 0 and in_info[now] == 1:
                answer[2] += 1
                break
            
            prev = now
            for next_node in out_info[now]:
                deq.append(next_node)

    return answer

# 도넛 모양 그래프는 n개의 정점과 n개의 간선이 있음.
# 아무나 한 정점에서 시작해서 나머지 n-1개의 정점들을 한 번씩 방문한 뒤, 원래 출발했던 정점으로 돌아오면 끝.


# 막대모양 그래프는 n개의 정점과 n-1개의 간선이 있음.
# 임의의 한 점에서 출발해서 계속 따라가서 나머지 정점들을 모두 방문하는 단 하나의 정점이 존재함.


# 8자묘양 그래프는 2n+1개의 정점과 2n+2개의 간선이 있음.
# 크기가 동일한 2개의 도넛모양 그래프에서 정점을 하나씩 골라 결합한 형태임.


# 간선을 따라 가면서 시작지점으로 돌아오면 도넛 모양 그래프
# 간선을 따라 가면서 시작지점으로 돌아오지 못하면 막대 모양 그래프
# 간선을 따라 가면서 나가는 간선이 2개인 정점을 만나면 8자 그래프(?)


# 시작 지점을 어떻게 구하지 ?? -> 들어오는 간선이 없는 곳이 시작 지점이네.
# 들어오는 간선이 없는 곳 중에서 나가는 간선이 많은 곳인가 ..?
# 시작 지점에서 나가는 포인트 개수의 총 합은 총 그래프의 개수.


# 들어오는 간선이 없는 경우 1. 시작 지점 2. 막대 모양 그래프의 시작 지점
# 들어오는 간선이 없고, 나가는 간선 1개 이상 있을 경우 = 시작 지점
# 들어오는 간선이 없고, 나가는 간선이 1개 있을 경우 = 막대 모양 그래프의 시작 지점


# 그럼 1개씩 있는 경우를 어떻게 거르지?
# 아하 도넛 모양, 막대모양, 8자 모양 그래프의 합은 2 이상이구나.
# 그럼 1개가 있을 경우 무조건 막대 모양 그래프 시작 지점.


# 막대 모양 그래프는 이전 간선을 저장 했다가 다음 간선이 이전 간선과 같은 경우가 생겼을 경우 막대모양 그래프.

edges = [[2, 3], [4, 3], [1, 1], [2, 1]]
print(solution(edges))