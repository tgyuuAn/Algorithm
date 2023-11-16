def solution(board, moves):
    board = [[board[x][y] for x in range(len(board))] for y in range(len(board))]
    basket = []
    answer = 0
    
    for x in moves:
        for y in range(len(board)):
            if board[x-1][y]!=0:
                basket.append(board[x-1][y])
                board[x-1][y]=0
                break
                
        if len(basket)>=2:
            if basket[-1]==basket[-2]:
                basket.pop()
                basket.pop()
                answer+=2
                
    return answer