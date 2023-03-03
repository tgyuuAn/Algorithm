from math import factorial

def solution(n, k):
    dp = []
    table = [x for x in range(1,n+1)]

    now = 0
    while now < n :
        dp.append(factorial(now))
        now+=1

    answer = []
    while n!=0:
        now = dp[n-1]
        n-=1
        idx = k//now
        k = k% now

        if k!=0:
            answer.append(table.pop(idx))

        else:
            answer.append(table.pop(idx-1))
    
    return answer