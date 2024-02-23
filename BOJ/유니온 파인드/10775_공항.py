import sys
sys.setrecursionlimit(100000)

gate_count = int(sys.stdin.readline())
airplanes_count = int(sys.stdin.readline())
gate = [-1 for x in range(gate_count+1)]

def find_parent(num, gate):
    if num <= 0: return 0
    
    if num == gate[num]: return num
 
    parent = find_parent(gate[num], gate)
    gate[num] = parent
    return parent

def union_find(num, num2, gate):
    x = find_parent(num, gate)
    y = find_parent(num2, gate)

    x, y = max(x, y), min(x, y)
    gate[x] = y

    if x == 0: return False
    return True

answer = 0
for idx in range(1,airplanes_count+1):
    _input = int(sys.stdin.readline())
    if union_find(_input, _input-1, gate): answer += 1
    else: break
        
print(answer)