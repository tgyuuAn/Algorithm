def solution(genres, plays):
    dict = {}
    dict_max = {}
    answer = []
    for i in range(len(genres)):
        if genres[i] not in dict:
            dict[genres[i]] = [[i,plays[i]]]
        else:
            dict[genres[i]].append([i,plays[i]])

    for i in dict:
        tot =0
        for j in dict[i]:
            tot += j[1]
        dict_max[i]=tot
        dict[i].sort(reverse=True, key=lambda x: x[1])
        
    dict_max = sorted(list(dict_max.items()), reverse = True, key = lambda x:x[1])

    for i in dict_max:
        count = 0
        while dict[i[0]]:
            if len(dict[i[0]])==0 or count ==2:
                break
            else:
                answer.append(dict[i[0]].pop(0)[0])
                count +=1

    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres,plays))