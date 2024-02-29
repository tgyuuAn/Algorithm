import sys

def input():
    return sys.stdin.readline()

N = int(input())
numbers = list(map(int,input().split()))
sequence = [numbers[0]]
temp = [1]

def check(element, number):
    if element <= number: return True
    return False

def add_numbers(element, sequence):
    if element > sequence[-1]:
        temp.append(len(sequence)+1)
        sequence.append(element)

    else:
        left = -1
        right = len(sequence)
        answer = 0
        while left+1<right:
            mid = (left+right)//2

            # 만약 현재 넣으려고 하는 요소가 mid보다 작다면
            if check(element, sequence[mid]):
                right = mid
                answer = mid

            else: left = mid

        temp.append(answer+1)
        sequence[answer] = element

for idx in range(1,N):
    add_numbers(numbers[idx],sequence)

now = len(sequence)
for number, idx in zip(numbers[::-1],temp[::-1]):
    if now == idx:
        sequence[idx-1] = number
        now -= 1
        
    if now == 0: break

print(len(sequence))
print(*sequence)