dedications = []
max_score = 0

def dfs(remain_count, idx, apeach_scores, ryan_scores):
    global max_score, dedications

    if idx == len(apeach_scores)-1:
        print(remain_count, idx, end=" ")
        print(f"라이언 점수판 : {ryan_scores}")

        ryan_scores[-1] = remain_count
        score_gap = calculate_score(apeach_scores, ryan_scores)
        
        if score_gap == 0:
            ryan_scores[-1] = 0
            return

        if score_gap > max_score:
            dedications = [ryan_scores.copy()]
            max_score = score_gap
        
        elif score_gap == max_score:
            dedications.append(ryan_scores.copy())
        
        ryan_scores[-1] = 0
        return
    
    if remain_count >= apeach_scores[idx]+1:
        remain_count -= apeach_scores[idx]+1
        ryan_scores[idx] = apeach_scores[idx]+1
        dfs(remain_count, idx+1, apeach_scores, ryan_scores)
        remain_count += apeach_scores[idx]+1
        ryan_scores[idx] = 0
    
    dfs(remain_count, idx+1, apeach_scores, ryan_scores)

def calculate_score(apeach_scores, ryan_scores):
    score = 0
    for idx, (ryan_score, apeach_score) in enumerate(zip(ryan_scores, apeach_scores)):
        if ryan_score == apeach_score == 0: continue
        if apeach_score >= ryan_score: score -= (10-idx)
        else: score += (10-idx)
    return score

def solution(n, info):
    global dedications
    
    dfs(n,0,info, [0 for _ in range(len(info))])
    dedications.sorted(key = lambda x : (x[-1],x[-2],x[-3],x[-4],x[-5],x[-6],x[-7],x[-8],x[-9],x[-10],x[-11],x[-12]), reverse= True)
    return [-1] if not dedications else dedications[0]

n = 9
info = [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]
print(f"actual : {solution(n,info)}")
print(f"expected = [1, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0]")