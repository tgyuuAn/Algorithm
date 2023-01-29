def solution(m, n, puddles):

    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for x, y in puddles:
        dp[y][x] = -1

    dp[1][1] = 1
    
    for y in range(1,n+1):
        for x in range(1,m+1):
            
            if x==1 and y==1:
                continue

            elif dp[y][x]<0:
                continue

            else:
                tem1 = 0 if dp [y-1][x] <0 else dp[y-1][x]
                tem2 = 0 if dp [y][x-1] <0 else dp[y][x-1]
                dp[y][x] = tem1 + tem2
                
    return dp[-1][-1]%1_000_000_007