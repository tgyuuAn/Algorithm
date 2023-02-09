from collections import deque

def reverse(strings):
    r = {"(":")", ")": "("}
    return [r[s] for s in strings]


def solution(w):

    tempW = deque(w)
    dic = {"(" : 0}
    flag = True
    while tempW:
        temp = tempW.popleft()
        if temp=="(":
            dic[temp] +=1

        elif temp==")":
            if dic["("]==0:
                flag = False
                break
            else:
                dic["("] -= 1
       
    if flag:
        return w

    if len(w)==0:
        return ""

    answer = ""
    dic = {"(" : 0, ")" : 0}
    dequeW = deque(w)
    u = deque()

    while dequeW:
        temp = dequeW.popleft()
        dic[temp] +=1
        u.append(temp)

        if dic["("] >= 1 and dic[")"] >= 1 and dic["("] == dic[")"]:
            break

    
    v= dequeW
    print("".join(u))
    print(v)
    flag = True
    dic = {"(" : 0}
    tempU = u.copy()
    while tempU:
        temp = tempU.popleft()
        if temp=="(":
            dic[temp] +=1

        elif temp==")":
            if dic["("]==0:
                flag = False
                break
            else:
                dic["("] -= 1

    if flag:
        print("u는 올바른 문자열입니다.")
        answer += "".join(u)
        v = "".join(v)
        
        print(v)
        
        if len(v)!=0:
            answer+=solution(v)

    else:
        tempV = "("
        if len(v)!=0:
            v= "".join(v)
            tempV += solution(v)
        tempV += ")"
        u.pop()
        u.popleft()
        u=reverse(u)
        u="".join(u)
        tempV += u
        v=tempV
        answer+=v


    print(u,v)

    return answer

w = "()))((()"
solution(w)