from collections import defaultdict

temp = 0
def dfs(y, x, visited, land, col_info):
    global temp

    n_y = len(land)
    n_x = len(land[0])

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    for dir in range(4):
        new_y = y+dy[dir]
        new_x = x+dx[dir]

        if new_y < 0 or new_y >= n_y: continue
        if new_x < 0 or new_x >= n_x: continue
        if (new_y, new_x) in visited: continue
        if land[new_y][new_x] == 0: continue

        visited.add((new_y, new_x))
        col_info.add(new_x)
        temp += 1
        dfs(new_y, new_x, visited, land, col_info)

def solution(land):
    global temp

    visited = set()
    
    n_row = len(land)
    n_col = len(land[0])
    oil_info = defaultdict(int)

    for row in range(n_row):
        for col in range(n_col):
            if land[row][col] == 1 and (row, col) not in visited:
                temp = 1
                col_info = {col,}
                visited.add((row,col))
                dfs(row, col, visited, land, col_info)

                print(temp, col_info)

                for c in col_info:
                    oil_info[c] += temp

            print(oil_info)
    return max(list(oil_info.values()))

land = [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]
print(solution(land))