from heapq import *

total_test_case = int(input())

for _ in range(total_test_case):
    total_numbers_count = int(input())

    max_heap = []
    min_heap = []
    numbers = []
    answer = []
    
    while len(numbers) != total_numbers_count:
        numbers.extend(list(map(int,input().split())))

    for idx,number in enumerate(numbers):
        if len(max_heap) == len(min_heap): heappush(max_heap, -1*number)
        else: heappush(min_heap, number)

        if min_heap and -1*max_heap[0] > min_heap[0]:
            a = heappop(max_heap)
            b = heappop(min_heap)
            heappush(min_heap, -1*a)
            heappush(max_heap, -1*b)

        if idx%2==0: answer.append(-1*max_heap[0])

    print(len(answer))
    for start_idx in range(0,len(answer),10):
        print(*answer[start_idx:start_idx+10])