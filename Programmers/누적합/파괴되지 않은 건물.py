def solution(board, skill):
    temp = [[0 for _ in range(1001)] for _ in range(1001)]
    
    for _type, r1, c1, r2, c2, degree in skill:
        if _type == 1:
            temp[r1][c1] += -1*degree
            temp[r1][c2+1] += degree
            temp[r2+1][c1] += degree
            temp[r2+1][c2+1] += -1*degree
            
        else: 
            temp[r1][c1] += degree
            temp[r1][c2+1] += -1*degree
            temp[r2+1][c1] += -1*degree
            temp[r2+1][c2+1] += degree
            
    for t_r in range(len(temp)):
        acc = 0
        for t_c in range(len(temp[0])):
            acc += temp[t_r][t_c]
            temp[t_r][t_c] = acc
            
    for t_c in range(len(temp[0])):
        acc = 0
        for t_r in range(len(temp)):
            acc += temp[t_r][t_c]
            temp[t_r][t_c] = acc
    
    answer = 0
    for r in range(len(board)):
        for c in range(len(board[0])):
            board[r][c] += temp[r][c]
            if board[r][c] > 0: answer += 1
        
    return answer