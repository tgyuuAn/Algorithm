def solution(record):
    name_dict = {}
    logic = []
    answer = []
    for i in record:
        i=i.split()
        if i[0]=="Enter" or i[0]=="Change":
            name_dict[i[1]]=i[2]
            logic.append([i[1],"Enter"])
        elif i[0]=="Leave":
            logic.append([i[1],"Leave"])
            
    for i in logic:
        if i[1]=="Enter":
            answer.append(f"{name_dict[i[0]]}님이 들어왔습니다.")
        elif i[1]=="Leave":
            answer.append(f"{name_dict[i[0]]}님이 나갔습니다.")
            
    return answer