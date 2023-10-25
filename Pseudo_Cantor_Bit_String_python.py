def solution(n, l, r):
    return recursion(n,r) - recursion(n,l-1)


def recursion(n,pos):
    if n==1:
        return "11011"[:pos].count("1")
    
    a,b = divmod(pos, 5**(n-1))
    count = 0
    if a <= 1:
        count = 4**(n-1) * a + recursion(n-1,b)
        
    if a == 2:
        count = 4**(n-1) * a
        
    if a > 2:
        count = 4**(n-1) * (a-1) + recursion(n-1,b)
        
    return count