def solution(arr):
    dx = [0,1,1]
    dy = [1,0,1]
    n = len(arr)
    dic = {0:0,1:0}
    for x in arr:
        for y in x:
            dic[y] +=1

    width = len(arr)
    while width!=1:
        for x in range(0,n,width):
            for y in range(0,n,width):
                now = arr[x][y]
                if now == "펑!":
                    continue

                flag = True
                for i in range(3):

                    for w in range(1,width):
                        nx = x+dx[i]*w

                        for e in range(1,width):
                            ny = y+dy[i]*e
                            if now != arr[nx][ny]:
                                flag = False
                                break

                        if flag == False:
                            break

                    if flag ==False:
                        break

                if flag:
                    dic[now]-=(width**2)-1
                    for i in range(3):

                        for w in range(1,width):
                            nx = x+dx[i]*w

                            for e in range(1,width):
                                ny = y+dy[i]*e
                                arr[nx][ny] = "펑!"
        width //= 2

    return [dic[0],dic[1]]