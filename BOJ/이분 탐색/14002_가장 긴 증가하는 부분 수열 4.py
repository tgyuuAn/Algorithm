import sys

def input(): return sys.stdin.readline()

N = int(input())
numbers = list(map(int,input().split()))
sequence = [numbers[0]]
record = [1]

def check(element, number):
    if element <= number: return True
    return False

def add_number(element, sequence):
    if element > sequence[-1]:
        sequence.append(element)
        record.append(len(sequence))

    else:
        left = -1
        right = len(sequence)
        answer = right-1
        while left+1<right:
            mid = (left+right)//2

            if check(element, sequence[mid]):
                right = mid
                answer = mid

            else: left = mid
            
        sequence[answer] = element
        record.append(answer+1)

for number in numbers[1:]:
    add_number(number, sequence)

now = len(sequence)
for number, idx in zip(numbers[::-1], record[::-1]):
    if idx == now:
        sequence[idx-1] = number
        now -= 1

    if now == 0: break

print(len(sequence))
print(*sequence)