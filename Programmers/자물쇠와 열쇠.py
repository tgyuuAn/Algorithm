def solution(key, lock):
    
    for key_row in key:
        print(key_row)

    answer = True
    return answer

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]	
solution(key, lock)