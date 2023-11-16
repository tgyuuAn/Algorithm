def solution(id_list, reports, k):
    dic = dict()
    answer = dict()
    log = set()
    
    for x in id_list:
        dic[x] = []
        answer[x] = 0
    
    for report in reports:
        if report not in log:
            log.add(report)
            a,b = report.split()
            dic[b].append(a)
            
    for x in dic:
        if len(dic[x]) >= k:
            for y in dic[x]:
                answer[y] += 1
                    
    return list(answer.values())