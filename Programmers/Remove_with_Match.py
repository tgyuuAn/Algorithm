def solution(s):
    s = list(s)
    tempList = []

    while s:
        if len(tempList) == 0:
                tempList.append(s.pop())
        else:
            temp = s.pop()
            if tempList[-1] == temp:
                tempList.pop()

            else: tempList.append(temp)

    if tempList==[]:
        return 1
    else: return 0