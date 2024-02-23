first = input()
second = input()

DP = [[0 for _ in range(len(second)+1)] for _ in range(len(first)+1)]

for row in range(1,len(first)+1):
    for col in range(1,len(second)+1):
        if first[row-1] == second[col-1]:
            DP[row][col] = DP[row-1][col-1]+1

        else:
            DP[row][col] = max(DP[row-1][col], DP[row][col-1])

print(DP[-1][-1])

if DP[-1][-1] > 0:
    LCS = ""
    row_idx = len(first)
    col_idx = len(second)
    
    print(first, second, row_idx, col_idx)
    
    while True:
        if first[row_idx-1] == second[col_idx-1]:
            LCS = first[row_idx-1] + LCS
            row_idx, col_idx = row_idx -1, col_idx -1
    
            if len(LCS) == DP[-1][-1]: break
    
        else:
            if DP[row_idx-1][col_idx] > DP[row_idx][col_idx-1]: row_idx -= 1
            else: col_idx -=1
    
    print(LCS)