class Solution:
    def check(self, start_row, start_col, row_sum, col_sum, grid):
        if start_row + 3 >= len(row_sum): return False
        if start_col + 3 >= len(row_sum[0]): return False

        temp_row_sum = row_sum[start_row+1][start_col+3]-row_sum[start_row+1][start_col]
        for idx in range(1,3):
            temp = row_sum[start_row+1+idx][start_col+3]-row_sum[start_row+1+idx][start_col]
            if temp_row_sum != temp: return False

        temp_col_sum = col_sum[start_row+3][start_col+1]-col_sum[start_row][start_col+1]
        if temp_row_sum != temp_col_sum: return False
        for idx in range(1,3):
            temp = col_sum[start_row+3][start_col+1+idx]-col_sum[start_row][start_col+1+idx]
            if temp_col_sum != temp: return False

        temp_left_diagonal_sum = 0
        for idx in range(3):
            temp_left_diagonal_sum += grid[start_row+1+idx][start_col+1+idx]
        if temp_col_sum != temp_left_diagonal_sum: return False

        temp_right_diagonal_sum = 0
        for idx in range(3):
            temp_right_diagonal_sum += grid[start_row+idx+1][start_col+2-idx+1]
        if temp_col_sum != temp_right_diagonal_sum: return False

        return True

    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3: return 0
        grid.insert(0, [0 for _ in range(len(grid[0])+1)])
        for row_idx in range(1,len(grid)):
            grid[row_idx].insert(0, 0)

        row_sum = [[0 for _ in range(len(grid[0])+1)] for _ in range(len(grid)+1)]
        col_sum = [[0 for _ in range(len(grid[0])+1)] for _ in range(len(grid)+1)]
        left_diagonal_sum = [[0 for _ in range(len(grid[0])+1)] for _ in range(len(grid)+1)]
        right_diagonal_sum = [[0 for _ in range(len(grid[0])+1)] for _ in range(len(grid)+1)]
        
        for row in range(len(grid)):
            accmulate = 0
            for col in range(len(grid[row])):
                accmulate += grid[row][col]
                row_sum[row][col] = accmulate

        for col in range(len(grid[row])):    
            accmulate = 0
            for row in range(len(grid)):
                accmulate += grid[row][col]
                col_sum[row][col] = accmulate

        for row in range(len(grid)-2):
            for col in range(len(grid[row])-2):
                accmulate = 0
                for idx in range(max(len(grid), len(grid[0]))):
                    new_row = row + idx
                    new_col = col + idx
                    if new_row >= len(grid): break
                    if new_col >= len(grid[0]): break
                    accmulate += grid[new_row][new_col]
                    left_diagonal_sum[new_row][new_col] = accmulate

        for row in range(len(grid)-1, 1, -1):
            for col in range(len(grid[row])-2):
                accmulate = 0
                for idx in range(max(len(grid), len(grid[0]))):
                    new_row = row - idx
                    new_col = col + idx
                    if new_row < 0: break
                    if new_col >= len(grid[0]): break
                    accmulate += grid[new_row][new_col]
                    right_diagonal_sum[new_row][new_col] = accmulate

        answer = 0
        for row_idx in range(len(grid)):
            for col_idx in range(len(grid[0])):
                if self.check(row_idx, col_idx, row_sum, col_sum, grid):
                    answer += 1

        return answer

grid = [[5,5,5],[5,5,5],[5,5,5]]
solution = Solution()
print(solution.numMagicSquaresInside(grid))