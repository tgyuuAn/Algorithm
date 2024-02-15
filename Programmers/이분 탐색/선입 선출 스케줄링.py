def solution(n, cores):
    right = n*max(cores)
    left = 0
    answer = 0
    
    if n <= len(cores): return n

    n -= len(cores)

    while left < right:
        mid = (right + left) // 2

        temp = 0
        for idx,core in enumerate(cores):
            task = mid//core
            temp += task

        if temp < n:
            left = mid + 1
            
        elif temp >= n:
            right = mid

    total_time = right

    for core in cores:
        n -= (total_time-1)//core

    for idx, core in enumerate(cores):
        if (total_time % core == 0): n -= 1
        if n == 0:
            return idx+1