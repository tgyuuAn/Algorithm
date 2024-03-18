import sys

def input(): return sys.stdin.readline().rstrip()

N, K = map(int,input().split())

remain = [ x for x in range(1,N+1) ]
answer = []

index = 0
while remain:
    n = len(remain)
    index += K
    index = index % n 
    answer.append(remain[index-1])
    remain.pop(index-1)
    if index != 0: index -= 1
    
print("<", end="")
print(*answer, end="", sep=", ")
print(">", end="")