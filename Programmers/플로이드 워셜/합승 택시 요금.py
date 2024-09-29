def solution(n, s, a, b, fares):
    answer = 0
        
    table = [[int(1e9) for _ in range(n+1)] for _ in range(n+1)]
    
    for fare in fares:
        x, y, cost = fare
        table[x][y] = cost
        table[y][x] = cost

    for idx in range(n+1):
        table[idx][idx] = 0
        
    for mid in range(1,n+1):
        for start in range(1, n+1):
            for end in range(1, n+1):
                table[start][end] = min(table[start][end], table[start][mid] + table[mid][end])
    
    answer = int(1e9)
    for k in range(1,n+1):
        answer = min(answer, table[s][k] + table[k][a] + table[k][b])
    
    return answer