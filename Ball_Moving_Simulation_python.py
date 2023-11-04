LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

def solution(n, m, y, x, queries):
    
    left = x
    right = x
    top = y
    bottom = y
    
    for command, distance in queries[::-1]:
        if command == LEFT:
            if left == 0:
                right = min(right+distance,m-1)
                
            else:
                if left+distance < m:
                    right = min(right+distance,m-1)
                    left = min(left+distance,m-1)
                
                else: return 0
        
        elif command == RIGHT:
            if right == m-1:
                left = max(left-distance,0)
                
            else:
                if right-distance >= 0:
                    left = max(left-distance,0)
                    right = max(right-distance,0)
                
                else: return 0
            
        elif command == UP:
            if top == 0:
                bottom = min(bottom+distance,n-1)
                
            else:
                if top+distance < n:
                    top = min(top+distance, n-1)
                    bottom = min(bottom+distance, n-1)
                    
                else: return 0
            
        elif command == DOWN:
            if bottom == n-1:
                top = max(top-distance,0)
                
            else:
                if bottom-distance >= 0:
                    top = max(top-distance,0)
                    bottom = max(bottom-distance,0)
                
                else: return 0
    
    return ((right-left)+1) * ((bottom-top)+1)