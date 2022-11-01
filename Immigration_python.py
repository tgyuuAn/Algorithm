def solution(n, times):
    min_time = 1
    max_time = times[-1]*n
    answer = 0
    
    while min_time<=max_time:
        mid_time = (min_time+max_time)//2
        people = 0
        
        for time in times:
            people += mid_time//time
            
            if people>=n:
                break
                
        if people >= n:
            answer=mid_time
            max_time = mid_time -1
            
        elif people < n:
            min_time = mid_time +1
            
    return answer                
                
            