import math
import sys

sys.setrecursionlimit(100000)

def init(node, start, end, arr):
    # node가 leaf 노드일 경우 배열의 원소 값을 반환.
    if start == end:
        tree[node] = (arr[start], start)
        return tree[node]
 
    mid = (start+end)//2
    tree[node] = min(init(node*2, start, mid, arr), init(node*2+1, mid+1, end, arr))
    return tree[node]

def find_min(node, start, end, left, right):
    # start와 end는 전체 범위, left와 right는 최소값을 구할 범위이다.
    # 범위를 벗어날 경우, 구할 필요가 없다.
    if left > end or right < start: 
        return (1000000001,0)

    elif left <= start and end <= right:
        return tree[node]

    mid = (start+end)//2
    return min(find_min(node*2, start, mid, left, right), find_min(node*2+1, mid+1, end, left, right))

def divide_and_conquer(start, end, total_count):
    if end < start:
        return 0

    min_height, idx = find_min(1,1,total_count,start,end)
    now = (end-start+1)*min_height

    return max(now, divide_and_conquer(start, idx-1, total_count), divide_and_conquer(idx+1,end,total_count))

while True:
    heights = list(map(int,input().split()))
    total_count = heights[0]
    heights[0] = 0
    if total_count == 0:
        break
    
    size = 2**(math.ceil(math.log(len(heights),2))+1)
    tree = [0 for _ in range(size)]
    init(1,1,total_count,heights)
    print(divide_and_conquer(1,total_count,total_count))