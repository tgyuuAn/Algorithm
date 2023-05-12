def solution(arr, query):
    for x in range(len(query)):
        #짝수 일경우 인덱스 뒷부분 잘라냄
        if x%2==0:
            arr = arr[:query[x]+1]
            
        #홀수일경우 인덱스 앞부분 잘라냄
        elif x%2==1:
            arr = arr[query[x]:]
    return arr