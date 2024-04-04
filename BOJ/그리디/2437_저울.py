import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
weights = sorted(list(map(int, input().split())))

temp = 0
for idx, weight in enumerate(weights):    
    if weight > temp+1: 
        temp += 1
        break

    else: temp += weight
else:
    temp += 1
    
print(temp)
