def solution(board):
    n = len(board[0])
    m = len(board)
    dp = [[0 for _ in range(n)] for _ in range(m)]
    answer = 0
    
    for x in range(n):
        dp[0][x] = board[0][x]
        answer = max(answer,dp[0][x])
    
    for y in range(m):
        dp[y][0] = board[y][0]
        answer = max(answer,dp[0][x])
        
    for y in range(1,m):
        for x in range(1,n):
            if board[y][x] == 1:
                dp[y][x] = min(dp[y-1][x-1],dp[y-1][x],dp[y][x-1])+1
                answer = max(answer,dp[y][x])

    return answer **2