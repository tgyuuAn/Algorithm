from collections import deque

def numeral(m,n):
    temp = ""
    while m>=n:
        m,x = divmod(m,n)
        print(x)
        if x>=10:
            x= chr(55+x)

        temp = str(x)+temp

    if m>=10:
        m= chr(55+m)
    temp = str(m)+temp
    
    return list(temp)


def solution(n, t, m, p):
    now = 1
    nowNum = 0
    temp = deque()
    answer = ""

    while t!=0:

        if not temp:
            temp.extend(numeral(nowNum,n))
            nowNum += 1

        if now > m:
            now %= m
            

        if now == p:
            answer = answer + temp.popleft()
            t -= 1
            
        else:
            temp.popleft()

        now += 1

    print(answer)

    return 

n,t,m,p = 16,16,2,1
solution(n,t,m,p)