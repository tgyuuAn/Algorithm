import sys

def input(): return sys.stdin.readline()

N = int(input())
port = list(map(int,input().split()))
new_port = [port[0]]

def check(element, number):
    if element <= number: return True
    else: return False

def add_port(element, new_port):
    if element > new_port[-1]:
        new_port.append(element)

    else:
        left = -1
        right = len(new_port)
        answer = right-1

        while left+1<right:
            mid = (left+right)//2

            if check(element, new_port[mid]):
                right = mid
                answer = mid

            else: left = mid

        new_port[answer] = element

for i in port[1:]:
    add_port(i, new_port)

print(len(new_port))