score = 0
max_list = []
def dfs(idx, remain_shoot_count, apeach_shoot, ryan_shoot):
    global score, max_list

    if idx == 11:
        accumulate = 0
        for i, count in enumerate(ryan_shoot):
            if apeach_shoot[i] > 0 and count > apeach_shoot[i]:
                accumulate += (10-i) * 2
                continue

            elif apeach_shoot[i] == 0 and count > apeach_shoot[i]:
                accumulate += (10-i)

        if accumulate > score:
            score = accumulate
            max_list = ryan_shoot[:]
        return
    
    if remain_shoot_count >= apeach_shoot[idx] + 1:
        ryan_shoot[idx] = apeach_shoot[idx] + 1
        remain_shoot_count -= apeach_shoot[idx] + 1
        dfs(idx+1, remain_shoot_count, apeach_shoot, ryan_shoot)
        ryan_shoot[idx] = 0
        remain_shoot_count += apeach_shoot[idx] + 1
        
    dfs(idx+1, remain_shoot_count, apeach_shoot, ryan_shoot)

def solution(n, info):
    global score, max_list

    ryan_shoot = [0 for _ in range(11)]
    dfs(0,n,info,ryan_shoot)
    
    lose_check = 0
    for idx, (apeach, ryan) in enumerate(zip(info, max_list)):
        if apeach >= ryan:
            lose_check += (10-idx)

        else:
            lose_check -= (10-idx)

    return max_list if lose_check < 0 else [-1]

n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
print(solution(n,info))