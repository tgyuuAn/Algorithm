def solution(n, m, section):
    answer = 0
    board = [0 for _ in range(n+1)]
    
    for x in section:
        board[x] = 1
    
    for x in range(1,n-(m-1)+1):
        if board[x] == 1:
            for y in range(x,x+m):
                board[y] = 0
            answer += 1

    for x in range(n,m-1,-1):
        if board[x] == 1:
            for y in range(x,x-m,-1):
                board[y] = 0
            answer += 1

    return answer