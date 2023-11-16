import math

def solution(arrayA, arrayB):
    answer = 0
    gcdA = 0
    gcdB = 0
    
    for x in arrayA:
        gcdA = math.gcd(gcdA,x)
    
    for y in arrayB:
        gcdB = math.gcd(gcdB,y)
        
    for z in arrayB:
        if z%gcdA==0:
            gcdA = 0
            break
    for z in arrayA:
        if z%gcdB==0:
            gcdB = 0
            break
    
    return max(gcdA,gcdB)