def solution(str_list):
    for idx,string in enumerate(str_list):
        if string == "l":
            return str_list[:idx]
        elif string =="r":
            return str_list[idx+1:]
    return []