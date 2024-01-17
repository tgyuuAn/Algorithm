from heapq import *

def solution(food_times, k):
    food_times = [(time, idx+1) for idx, time in enumerate(food_times)]
    heapify(food_times)

    prev = 0
    while food_times:
        peak = food_times[0][0]
        # print(food_times, k, peak, prev)
        if k-len(food_times)*(peak-prev) < 0:
            break
        
        k -= len(food_times)*(heappop(food_times)[0]-prev)
        prev = peak
    
    if len(food_times) == 0:
        return -1
    
    while k >= len(food_times):
        k -= len(food_times)

    # print(k)
    # print(food_times)

    food_times.sort(key = lambda x : x[1])

    return food_times[k][1]