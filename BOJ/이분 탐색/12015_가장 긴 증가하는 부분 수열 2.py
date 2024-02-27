import sys

N = int(sys.stdin.readline())
numbers = (list(map(int,sys.stdin.readline().split())))
sequence = [numbers[0]]

def add_sort(list, new):
    if list[-1] < new: list.append(new)
    else: 
        left = -1
        right = len(list)
        answer = 0
        while left+1<right:
            mid = (left+right)//2

            if check(new, mid): 
                right = mid
                answer = mid
            else: left = mid
        list[answer] = new
    return

def check(element, mid):
    if element < sequence[mid]: return True
    return False

for number in numbers[1:]:
    add_sort(sequence, number)
    
print(len(sequence))