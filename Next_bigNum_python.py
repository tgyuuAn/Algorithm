def solution(n):

    target = bin(n)[2:].count("1")
    print(target)

    while True:
        n += 1
        temp = bin(n)[2:].count("1")
        if temp==target:
            return n