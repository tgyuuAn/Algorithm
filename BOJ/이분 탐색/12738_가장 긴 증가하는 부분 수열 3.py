import sys

def input(): return sys.stdin.readline()

N = int(input())
numbers = list(map(int,input().split()))
sequence = [numbers[0]]


def check(element, number):
    if element <= number: return True
    return False

def add_numbers(element, sequence):
    if element > sequence[-1]:
        sequence.append(element)

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

for number in numbers[1:]:
    add_numbers(number, sequence)
    print(sequence)

print(len(sequence))