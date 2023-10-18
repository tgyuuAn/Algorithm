def solution(board):

    def check(player):

        #열 체크
        for col in range(3):
            if player == board[0][col] == board[1][col] == board[2][col]:
                return True

        #행 체크
        for row in range(3):
            if player == board[row][0] == board[row][1] == board[row][2]:
                return True

        # 오른쪽 위 -> 왼쪽 대각선 체크
        temp = [board[x][x]==player for x in range(3)]
        if all(temp):
            return True

        # 왼쪽 위 -> 오른쪽 대각선 체크
        temp = [board[2-x][x]==player for x in range(3)]
        if all(temp):
            return True

        return False

    dic = {"O" : 0, "X" : 0}
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y].isalpha():
                dic[board[x][y]] += 1

    if dic["O"] < dic["X"]:
        return 0

    if dic["O"] > dic["X"] + 1:
        return 0

    if  dic["O"] > dic["X"]:
        #O의 개수가 X의 개수보다 1개만 많을 경우, X는 완성되어 있으면 안됨
        if check("X"):
            return 0

    if dic["O"] == dic["X"]:
        #O와 X의 개수가 같을 경우 O는 완성되어 있으면 안됨
        if check("O"):
            return 0
        
    return 1