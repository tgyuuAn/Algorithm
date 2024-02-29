import sys

def input():
    return sys.stdin.readline()

N = int(input())
soldiers = list(map(int,input().split()))
sorted_soldiers = [soldiers[0]]

def check(element, number):
    if element > number: return True
    return False

def add_soldier(element, soldiers):
    if element < soldiers[-1]:
        soldiers.append(element)

    else:
        left = -1
        right = len(soldiers)
        answer = 0
        while left+1<right:
            mid = (left+right)//2

            if check(element, sorted_soldiers[mid]):
                right = mid
                answer = mid

            else: left = mid

        soldiers[answer] = element

for power in soldiers[1:]:
    add_soldier(power, sorted_soldiers)

print(len(soldiers) - len(sorted_soldiers))