def solution(n):
    board = [[True for _ in range(n)] for _ in range(n)]
    answer = 0

    def dfs(row,col,count):
        nonlocal answer

        if row==n:
            if count==n:
                answer += 1
            return

        continue_flag = False
        for x in range(n):

            #세로 체크
            for idx in range(n):
                if board[idx][x] == False:
                    continue_flag = True
                    break

            if continue_flag:
                continue_flag = False
                continue

            #대각선 체크
            new_col = x
            new_row = row

            while True:
                new_row -= 1
                new_col -= 1

                if new_row < 0 or new_row >= n:
                    break

                if new_col < 0 or new_col >= n:
                    break

                if board[new_row][new_col] == False:
                    continue_flag = True
                    break

            if continue_flag:
                continue_flag = False
                continue

            #대각선 체크
            new_row = row
            new_col = x

            while True:
                new_row -= 1
                new_col += 1

                if new_row < 0 or new_row >= n:
                    break

                if new_col < 0 or new_col >= n:
                    break

                if board[new_row][new_col] == False:
                    continue_flag = True
                    break

            if continue_flag:
                continue_flag = False
                continue

            if continue_flag == True:
                continue_flag = False
                continue

            board[row][x] = False
            dfs(row+1,x,count+1)
            board[row][x] = True

    for x in range(n):
        board[0][x] = False
        dfs(1,x,1)
        board[0][x] = True

    return answer