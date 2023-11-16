from collections import defaultdict

def solution(gems):
    target = len(set(gems))
    dic = defaultdict(int)
    start=0
    end=-1
    n = len(gems)
    temp = []
    gapMin = 9876543210

    while True:
        if len(dic)!=target and end<n-1:
            end+=1
            dic[gems[end]]+=1

        if end==n-1 and len(dic)!=target:
            break

        if len(dic)==target:
            if gapMin != min(gapMin,end-start):
                temp.clear()
                gapMin = min(gapMin,end-start)

            temp.append([start+1,end+1])
            dic[gems[start]]-=1
            if dic[gems[start]] ==0:
                del dic[gems[start]]
            start+=1

        if end == n and start ==n:
            break

    temp.sort(key = lambda x:x[0])
    
    return temp[0]