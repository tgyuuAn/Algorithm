import heapq

a = [9,2,3]
heap = []
for i in a:
    heapq.heappush(heap,(-i,i))

print(heapq.heappop(heap)[1])
print(heap[0])
print(a[0])