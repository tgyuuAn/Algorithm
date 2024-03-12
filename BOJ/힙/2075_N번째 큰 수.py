import sys
from heapq import *

def input(): return sys.stdin.readline().rstrip()

N = int(input())

board = []
for _ in range(N):
    temp = list(map(lambda x : -1*int(x),input().split()))
    heapify(temp)
    
    # board가 비어있을 경우
    if not board: 
        board.extend(map(lambda x : -1*x, temp))
        heapify(board)
    
    else: 
        while -1*temp[0] > board[0]:
            heappop(board)
            heappush(board, -1*heappop(temp))
            
    # print(board)
            
print(board[0])