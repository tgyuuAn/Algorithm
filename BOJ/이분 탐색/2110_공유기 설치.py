import sys

total_house_count, total_router_count = map(int,sys.stdin.readline().rstrip())

houses = []
for _ in range(total_house_count):
    houses.append(int(sys.stdin.readline()))

houses.sort()

max_gap = (houses[-1] - houses[0]) // total_router_count

left = 0
right = max_gap+1

def check(mid, total_router_count, houses):
    prev = -1
    for house in houses:
        if prev == -1:
            prev = house
            total_router_count -= 1

        elif prev + mid <= house: 
            prev = house
            total_router_count -= 1

        else: continue

        if total_router_count <= 0:
            return True

    if total_router_count <= 0:
        return True
    
    return False

answer = 0
while left+1<right:
    mid = (left+right)//2

    if check(mid, total_router_count, houses):
        left = mid
        answer = mid

    else: right = mid

print(answer)