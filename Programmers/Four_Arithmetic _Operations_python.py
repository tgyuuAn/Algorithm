def solution(arr):

    n = len(arr)

    for i,x in enumerate(arr):
        if i%2==0:
            arr[i] = int(x)
    
    max_DP = [[ 0 for _ in range(n)] for _ in range(n)]
    min_DP = [[ 0 for _ in range(n)] for _ in range(n)]

    for idx in range(0,n,2):
        max_DP[idx][idx] = arr[idx]
        min_DP[idx][idx] = arr[idx]

    for x in range(3,n+1,2):
        for start in range(0,n,2):
            end = start + x - 1

            if end>=n:
                break

            max_candidates = []
            min_candidates = []
            for operator in range(start+1,end,2):
                
                if arr[operator] == "-":
                    max_candidates.append(max_DP[start][operator-1] - min_DP[operator+1][end])
                    min_candidates.append(min_DP[start][operator-1] - max_DP[operator+1][end])
                elif arr[operator] == "+":
                    
                    max_candidates.append(max_DP[start][operator-1] + max_DP[operator+1][end])
                    min_candidates.append(min_DP[start][operator-1] + min_DP[operator+1][end])

            max_DP[start][end] = max(max_candidates)
            min_DP[start][end] = min(min_candidates)

    return max_DP[0][-1]