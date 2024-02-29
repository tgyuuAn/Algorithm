import sys

def input(): return sys.stdin.readline()

N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
A.sort()

print(A)

wires = [A[0][1]]

def check(element, wire):
    if element <= wire: return True
    return False

def add_wire(element, wires):
    if element > wires[-1]:
        wires.append(element)

    else:
        left = -1
        right = len(wires)
        answer = right-1

        while left+1<right:
            mid = (left+right)//2

            if check(element, wires[mid]):
                right = mid
                answer = mid

            else: left = mid

        wires[answer] = element

for wire in A[1:]:
    add_wire(wire[1], wires)
    
print(N-len(wires))