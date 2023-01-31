def solution(n,a,b):
    count = 0
    while True:
        count+=1
        a = -(-a//2)
        b = -(-b//2)
        if a==b:
            return count

    return count