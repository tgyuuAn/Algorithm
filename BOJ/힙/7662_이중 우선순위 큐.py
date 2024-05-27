from heapq import *
from collections import defaultdict
import sys

def input(): return sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    K = int(input())
    min_heap = []
    max_heap = []
    elements = defaultdict(int)

    for _ in range(K):
        query = input()
        method, value = query.split()

        if method == "I":
            heappush(min_heap, int(value))
            heappush(max_heap, -1*int(value))
            elements[int(value)] += 1

        elif method == "D":
            if len(elements) == 0: continue

            # 최소값
            if value =="-1":
                while min_heap[0] not in elements:
                    heappop(min_heap)
                    
                popped = heappop(min_heap)
                elements[popped] -= 1
                if elements[popped] == 0: del elements[popped]

            # 최대값
            elif value =="1":
                while -1*max_heap[0] not in elements:
                    heappop(max_heap)
                    
                popped = heappop(max_heap)
                elements[-1*popped] -= 1
                if elements[-1*popped] == 0: del elements[-1*popped]

    if len(elements) == 0: print("EMPTY")
    else:
        remain = sorted(list(elements))
        print(remain[-1], remain[0])