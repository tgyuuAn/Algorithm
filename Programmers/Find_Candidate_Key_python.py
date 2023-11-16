from itertools import combinations

def solution(relation):
    
    answer = 0
    len_row = len(relation)
    len_col = len(relation[0])
    answer_set = set()
    
    for idx in range(1,len_col+1):
        for idx_cols in combinations(range(len_col),idx):
            
            answer_list = []
            for idx_row in range(len(relation)):
                
                temp_list = []
                for idx_col in idx_cols:
                    temp_list.append(relation[idx_row][idx_col])
                
                if temp_list not in answer_list:
                    answer_list.append(temp_list)

            if len(answer_list) == len_row:
                
                if len(answer_set) == 0:
                    answer_set.add(idx_cols)
                
                for candidate_key in answer_set:
                    
                    count = 0
                    
                    for candidate_element in candidate_key:
                        
                        if candidate_element not in idx_cols:
                            break
    
                        elif candidate_element in idx_cols:
                            count += 1
                    
                    if count == len(candidate_key):
                        break
                        
                    else:
                        continue
                        
                else:
                    answer_set.add(tuple(idx_cols))
                            
    return len(answer_set)