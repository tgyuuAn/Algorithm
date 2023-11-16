def solution(m, n, board):
    listBoard = [list(x) for x in board]
    answer = 0
    temp = set()

    dx = [1,0,1]
    dy = [0,1,1]

    flag = True
    while flag:
        flag = False
        temp = set()
        temp.clear()
    
        for x in range(m-1):
        
            for y in range(n-1):

                now =listBoard[x][y]
                
                if now == " ":
                    continue

                for z in range(3):
                    if now != listBoard[x+dx[z]][y+dy[z]]:
                        break
    
                else:
                    temp.add((x,y))
                    print(now, end= " ")
                    for z in range(3):
                        print(listBoard[x+dx[z]][y+dy[z]],end=" ")
                        temp.add((x+dx[z],y+dy[z]))
        
        temp = sorted(temp,key = lambda x : x[1])
    
        while temp:
            index = temp.pop()
            print(index)
            listBoard[index[0]][index[1]] = " "
            answer += 1
    
        print(listBoard)
    
        flag2 = True
        while flag2:
            flag2 = False
            for x in range(m-1):
                for y in range(n):
                    if listBoard[x+1][y] == " " and listBoard[x][y] != " ":
                        flag2 = True
                        flag = True
                        listBoard[x+1][y] = listBoard[x][y]
                        listBoard[x][y] = " "
        
        print(listBoard)
    return answer

m,n = 4,5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
solution(m,n,board)