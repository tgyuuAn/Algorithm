def isprime(n):
    if n==1:
        return False
    for i in range(2,int((n**0.5))+1):
        if n%i==0:
            return False
    return True

def isbelong(n,numbers):
    n=str(n)
    visited = [[n,False] for n in numbers]

    for i in n:
        if [i,False] not in visited:
            return False
        else :
            visited[visited.index([i,False])][1]=True 

    return True

def solution(numbers):
    temp = []
    for i in range(1,10**len(numbers)):
        if isbelong(i,numbers):
            if isprime(i):
                temp.append(i)
    print(temp)

solution("17")